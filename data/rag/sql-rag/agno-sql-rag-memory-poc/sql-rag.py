import os
import asyncio
import weaviate
from weaviate.auth import AuthApiKey

from langchain_core.runnables import Runnable
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from langchain_community.vectorstores import WeaviateVectorStore
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_core.tools import Tool
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_redis.chat_message_histories import RedisChatMessageHistory

# === ENV SETUP ===
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
os.environ["WEAVIATE_API_KEY"] = "your-weaviate-api-key"
os.environ["REDIS_URL"] = "redis://localhost:6379"

# === DATABASE CONNECTION ===
db_uri = "postgresql+psycopg2://user:password@localhost:5432/product_db"
db = SQLDatabase.from_uri(db_uri)

# === LLM ===
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# === VECTORSTORE (WEAVIATE) ===
weaviate_client = weaviate.Client(
    url="https://your-weaviate-instance.com",
    auth_client_secret=AuthApiKey(api_key=os.environ["WEAVIATE_API_KEY"])
)

vectorstore = WeaviateVectorStore(
    client=weaviate_client,
    index_name="SqlSchema",
    embedding=OpenAIEmbeddings(),
    text_key="text"
)

# Optional: Upload schema once
# schema_description = """The 'products' table contains: ... """
# vectorstore.add_texts([schema_description])

# === REDIS MEMORY ===
def get_redis_chat_history(session_id: str):
    return RedisChatMessageHistory(session_id=session_id, url=os.getenv("REDIS_URL"))

# === SQL TOOL SETUP ===
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
sql_tools = toolkit.get_tools()

# === PROMPT TEMPLATE ===
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a shopping assistant.\n"
               "Generate accurate SQL using the schema below:\n\n"
               "{schema_context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# === AGENT SETUP ===
agent = create_openai_functions_agent(llm=llm, tools=sql_tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=sql_tools, verbose=True)

# === MAIN ===
async def main():
    session_id = "user_123"
    user_input = "Show me blue dresses under $50."

    # Get chat memory
    chat_history = get_redis_chat_history(session_id)

    # Retrieve SQL schema from vector DB
    docs = vectorstore.similarity_search("products table schema", k=1)
    schema_context = docs[0].page_content if docs else ""

    # Run agent with inputs
    result = await agent_executor.ainvoke({
        "input": user_input,
        "chat_history": chat_history.messages,
        "schema_context": schema_context
    })

    # Store message history
    chat_history.add_message(HumanMessage(content=user_input))
    chat_history.add_message(AIMessage(content=result["output"]))

    print("Assistant:", result["output"])

if __name__ == "__main__":
    asyncio.run(main())
