from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.workflow import Workflow
from agno.utils.pprint import pprint_run_response

# Define the workflow
class MyWorkflow(Workflow):
    agent1 = Agent(model=OpenAIChat(id="gpt-4o-mini"))
    agent2 = Agent(model=OpenAIChat(id="gpt-4o-mini"))
    
    def my_custom_flow(self, message: str) -> Iterator[RunResponse]:
        # Agent 1 processes initial request
        result1 = self.agent1.run(message)
        yield result1

        # Extract the first message's content
        content1 = result1.messages[0].content if result1.messages else ""
        
        # Agent 2 processes the output of agent 1
        result2 = self.agent2.run(f"Analyze this: {content1}")
        yield result2

# Run the workflow
if __name__ == "__main__":
    workflow = MyWorkflow()
    response = workflow.my_custom_flow("Tell me about artificial intelligence")
    pprint_run_response(response, markdown=True, show_time=True)
