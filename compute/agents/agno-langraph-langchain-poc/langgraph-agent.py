import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

# Load environment variables from .env file
load_dotenv()

# Initialize the language model
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4", temperature=0)

# Define a custom tool
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers together."""
    return a * b

tools = [multiply]

# Create the agent
agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt="You are a helpful assistant that can perform mathematical operations."
)

# Run the agent with a sample input
response = agent.invoke(
    {"messages": [{"role": "user", "content": "What is 6 multiplied by 7?"}]}
)

print(response)
