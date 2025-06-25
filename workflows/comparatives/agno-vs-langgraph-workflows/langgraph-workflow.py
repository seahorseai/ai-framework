# langgraph_orchestration.py
import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Define the shape of the state
class QAState(TypedDict):
    question: str
    research_notes: str
    final_answer: str

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4",
    temperature=0)

# Agent 1: Researcher
def researcher_step(state: QAState) -> dict:
    question = state["question"]
    research_response = llm.invoke([HumanMessage(content=f"Research about: {question}")])
    return {"research_notes": research_response.content}

# Agent 2: Writer
def writer_step(state: QAState) -> dict:
    research = state["research_notes"]
    final_response = llm.invoke([HumanMessage(content=f"Explain this simply: {research}")])
    return {"final_answer": final_response.content}

# Build graph
builder = StateGraph(state_schema=QAState)

builder.add_node("research", researcher_step)
builder.add_node("write", writer_step)

builder.set_entry_point("research")
builder.add_edge("research", "write")
builder.add_edge("write", END)

graph = builder.compile()

# Execute
inputs = {"question": "Explain quantum computing in simple terms."}
result = graph.invoke(inputs)
print(result["final_answer"])
