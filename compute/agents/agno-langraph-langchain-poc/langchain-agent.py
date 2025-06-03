import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI LLM
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo",
    temperature=0
)

# Tool function: evaluates a math expression
def calculate_math(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"The result is: {result}"
    except Exception as e:
        return f"Error evaluating expression: {e}"

# Define the tool
tools = [
    Tool(
        name="Calculator",
        func=calculate_math,
        description="Evaluates basic math expressions. Input should be a valid Python expression like '3 * (4 + 2)'"
    )
]

# Create the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent
response = agent.run("What is (10 + 2) * 5?")
print(response)
