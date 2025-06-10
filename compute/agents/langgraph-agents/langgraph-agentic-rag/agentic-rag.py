# agentic-rag.py

import os
from dotenv import load_dotenv

# LangChain imports
from langchain.tools.retriever import create_retriever_tool
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# 🔁 Import LangGraph create_react_agent
from langgraph.prebuilt import create_react_agent

import langchain
langchain.verbose = True  # enable debug logs

# Load environment variables from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in your environment.")

# Create a sample text file
with open("state_of_the_union.txt", "w") as f:
    f.write("""
    Hello, my fellow citizens. Today, I want to talk about the future of our great nation.
    We are facing many challenges, including climate change, economic inequality, and global competition.
    Climate change is one of the most pressing issues of our time, and we must act now to ensure
    a better future for our children and grandchildren.
    """)

# 1️⃣ Load and split documents
loader = TextLoader("state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Embeddings and vectorstore
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectorstore = FAISS.from_documents(texts, embeddings)
retriever = vectorstore.as_retriever()

# Wrap retriever as a tool
retriever_tool = create_retriever_tool(
    retriever=retriever,
    name="doc_retriever",
    description="Search the document database for relevant information."
)

# Define LLM
llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

# 🔁 Create the agent using LangGraph's create_react_agent
agent_runnable = create_react_agent(llm, [retriever_tool])

# Run query
query = "What did the president say about climate change?"
response = agent_runnable.invoke({
    "messages": [
        ("system", "You are an intelligent agent who helps answer questions using a document retriever."),
        ("user", query)
    ]
})

print("\n--- Agent Response ---\n")
# Print the last AI message
for msg in response["messages"]:
    if msg.type == "AIMessage":
        print(msg.content)
        break