# agentic_rag.py

import os
from dotenv import load_dotenv

# LangChain imports
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.tools.retriever import create_retriever_tool
from langchain_core.prompts import ChatPromptTemplate

# Vectorstore and embeddings from langchain-community and langchain-openai
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

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
loader = TextLoader("state_of_the_union.txt")  # Replace with your text file
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectorstore = FAISS.from_documents(texts, embeddings)

# Create retriever from vectorstore
retriever = vectorstore.as_retriever()

# Wrap retriever as a LangChain tool
retriever_tool = create_retriever_tool(
    retriever=retriever,
    name="doc_retriever",
    description="Search the document database for relevant information."
)

# Define your LLM (GPT-4o or GPT-4-turbo)
llm = ChatOpenAI(
    model="gpt-4o",
    api_key=OPENAI_API_KEY,
)

# Prompt template for the agent - must include 'agent_scratchpad'
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an intelligent agent who helps answer questions using a document retriever."),
    ("user", "{input}"),
    ("assistant", "{agent_scratchpad}")
])

# Create the agent with the tools and prompt
agent = create_openai_functions_agent(
    llm=llm,
    tools=[retriever_tool],
    prompt=prompt
)

# Agent executor to run queries
agent_executor = AgentExecutor(
    agent=agent,
    tools=[retriever_tool],
    verbose=True
)

# Example query - replace with any question you want
query = "What did the president say about climate change?"

# Run the agent and print response
response = agent_executor.invoke({"input": query})

print("\n--- Agent Response ---\n")
print(response)
