

import os
import json
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Load environment variables
load_dotenv()

# Set up the agent with DuckDuckGo search capability
agent = Agent(
    model=OpenAIChat(id="gpt-4", api_key=os.getenv("OPENAI_API_KEY")),
    tools=[DuckDuckGoTools()],
    instructions="You are a helpful assistant that provides concise answers with relevant sources.",
    markdown=True,
)

# Ask a question
response = agent.run("What are the latest advancements in renewable energy?")

# Extract DuckDuckGo tool results (JSON string)
tool_results = None
for msg in response.messages:
    if msg.role == "tool" and msg.tool_name == "duckduckgo_news":
        tool_results = msg.content
        break

# Parse and structure results
if tool_results:
    try:
        articles = json.loads(tool_results)
        structured_output = []

        for article in articles:
            structured_output.append({
                "title": article.get("title"),
                "summary": article.get("body"),
                "url": article.get("url"),
                "source": article.get("source"),
                "published_at": article.get("date"),
                "image": article.get("image") or None
            })

        # Print the formatted JSON
        print(json.dumps(structured_output, indent=2))

    except json.JSONDecodeError as e:
        print("Error parsing tool result JSON:", e)
else:
    print("No DuckDuckGo tool response found.")
