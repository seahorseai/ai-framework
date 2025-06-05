# Complete Personal Shopper Agent using Agno (Updated for newer agno version)

from agno.agent import Agent, AgentMemory
from agno.models.openai import OpenAIChat
from agno.tools import tool

from agno.memory.v2.db.redis import RedisMemoryDb

from agno.vectordb.weaviate import Weaviate
import psycopg2

# --- Tool: Product Search via PostgreSQL ---
def query_products(question: str) -> str:
    sql = """
    SELECT name, price FROM products
    WHERE is_vegan = true AND size = 42
    ORDER BY price ASC LIMIT 1;
    """

    try:
        conn = psycopg2.connect(
            dbname="shop",
            user="your_user",
            password="your_password",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        conn.close()
        return f"{result[0]} — ${result[1]}" if result else "No matching products found."
    except Exception as e:
        return f"Database error: {str(e)}"




product_tool = Tool.from_function(
    name="search_products",
    description="Search vegan shoes by querying PostgreSQL.",
    func=query_products,
    inputs={"question": str},
)



# --- Redis Memory ---
memory = AgentMemory(
    db=RedisMemoryDb.from_url("redis://localhost:6379/0"),
    create_user_memories=True,
    update_user_memories_after_run=True,
    create_session_summary=True,
    update_session_summary_after_run=True,
)

# --- Knowledge from Weaviate ---
weaviate_kb = Weaviate.from_url("http://localhost:8080")  # ✅ Updated usage

# --- Create the Agent ---
agent = Agent(
    model=OpenAIChat(id="gpt-4o", api_key=os.getenv("OPENAI_API_KEY")),
    description="You are a helpful personal shopper. Help users find the right products.",
    tools=[product_tool],
    memory=memory,
    knowledge=weaviate_kb,  # ✅ Now uses the vector DB directly
    search_knowledge=True,
    read_chat_history=True,
    add_history_to_messages=True,
    num_history_responses=3,
    markdown=True,
)

# --- Load Knowledge (optional if needed) ---
if agent.knowledge is not None:
    agent.knowledge.load()

# --- Example Chat ---
if __name__ == "__main__":
    agent.print_response("Find me the cheapest vegan shoes in size 42.", stream=True)
