import os
from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize LangChain with OpenAI API
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Prompt and response
prompt = "Tell me a fun fact about space."
response = llm.invoke(prompt)

print("AI Response:", response)