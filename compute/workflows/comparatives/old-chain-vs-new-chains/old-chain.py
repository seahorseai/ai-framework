from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI  # Note: from langchain_openai, not langchain.llms
import os

# Step 1: Define the prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer this question in detail: {question}"
)

# Step 2: Create the chain using the LLM and the prompt
llm = OpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo-instruct")  # This is the correct argument name
chain = LLMChain(llm=llm, prompt=prompt)

# Step 3: Run the chain
response = chain.run("What is the capital of France?")
print(response)

