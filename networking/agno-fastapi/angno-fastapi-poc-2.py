from agno.app.fastapi.app import FastAPIApp
from agno.agent import Agent
from fastapi import FastAPI

# Create a basic agent
basic_agent = Agent(
    name="MyAgent",
    description="A simple demo agent"
)

# Create the FastAPI application
app = FastAPI(title="My Agno API")

# Create the FastAPI App with the agent
agno_app = FastAPIApp(
    agent=basic_agent,
    api_app=app,
    name="My Agno App",
    description="A demo Agno FastAPI application"
)

# Get the router and include it in the app
router = agno_app.get_async_router()
app.include_router(router)

# Run with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)