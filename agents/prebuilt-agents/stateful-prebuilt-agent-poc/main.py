from typing import TypedDict, List
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import create_react_agent

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

# Setup model and tools
llm = ChatOpenAI(model="gpt-4", temperature=0, api_key=api_key)
tools = [DuckDuckGoSearchRun()]

# Create ReAct agent with string prompt
# The agent will expect input as a list of messages under the "messages" key.
agent = create_react_agent(model=llm, tools=tools, prompt="You are a travel assistant that can use tools")

# Define state schema
class AgentState(TypedDict):
    # This key will hold the list of messages in the graph.
    messages: List[HumanMessage]

# Create a wrapper function to make the agent compatible with LangGraph
def run_agent(state: AgentState):
    """
    Wrapper function to run the LangChain agent with a state dictionary.
    """
   
    result = agent.invoke(state)
    final_message = result["messages"][-1]
    
    if hasattr(final_message, 'content'):
        return {"messages": [final_message]}
    else:
        return {"messages": [final_message]}

    

# Build LangGraph workflow
graph = StateGraph(AgentState)
graph.add_node("react_agent", run_agent)  # Use our wrapper function
graph.add_edge(START, "react_agent")
graph.add_edge("react_agent", END)

# Compile and invoke
app = graph.compile()
result = app.invoke({"messages": [HumanMessage(content="What are the most popular places to visit in Spain?")]})
print(result["messages"][-1].content)