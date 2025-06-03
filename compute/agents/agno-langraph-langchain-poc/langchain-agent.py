import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType, load_tools
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI LLM
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo", temperature=0)

# Load some basic tools (calculator, etc.)
tools = load_tools(["llm-math"], llm=llm)

# Create a zero-shot reactive agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent
response = agent.run("What is (10 + 2) * 5?")
print(response)
