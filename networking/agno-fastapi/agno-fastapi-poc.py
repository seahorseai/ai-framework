from agno.agent import Agent
from agno.app.fastapi.app import FastAPIApp
from agno.app.fastapi.serve import serve_fastapi_app
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


basic_agent = Agent(
    name="Basic Agent",
    model=OpenAIChat(id="gpt-4o", api_key=os.getenv("OPENAI_API_KEY")), # Ensure OPENAI_API_KEY is set
    add_history_to_messages=True,
    num_history_responses=3,
    add_datetime_to_instructions=True,
    markdown=True,
)

# Async router by default (use_async=True)
app = FastAPIApp(agent=basic_agent).get_app()

# For synchronous router:
# app = FastAPIApp(agent=basic_agent).get_app(use_async=False)

if __name__ == "__main__":
    # Assumes script is `basic_app.py`; update if different.
    serve_fastapi_app("agno-fastapi-poc:app", port=8001, reload=True)