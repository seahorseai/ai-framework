import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Load environment variables from .env file
load_dotenv()

# Initialize the agent
agent = Agent(
    model=OpenAIChat(id="gpt-4", api_key=os.getenv("OPENAI_API_KEY")),
    tools=[DuckDuckGoTools()],
    instructions="You are a helpful assistant that provides concise answers with relevant sources.",
    markdown=True,
)

# Use the agent to answer a question
response = agent.run("What are the latest advancements in renewable energy?")
print(response)
