from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Step 1: Prompt template
prompt = PromptTemplate.from_template("Answer this question in detail: {question}")

# Step 2: Define LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Step 3: Pipe together steps
chain = (
    RunnablePassthrough.assign(question=lambda x: x["input"])  # rename input -> question
    | prompt
    | llm
    | StrOutputParser()  # parse the model output to a string
)

# Step 4: Run the pipe
response = chain.invoke({"input": "What is the capital of France?"})
print(response)
