# imports 
from agno.agent import Agent
from agno.models.groq import Groq
from fastapi import FastAPI

agent = Agent(
    name= "Basic Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    description="You are a helpful assistant.",
    markdown=True,
)

from image_agent import agent1
from agno.playground import Playground, serve_playground_app

# app = Playground(agents=[agent, agent1]).get_app()

app = FastAPI()

@app.get("/")
async def root():
    return  {"message": "Server is up"}

@app.get("/ask")
async def ask(query: str):
    response = agent.run(query)
    return {"response": response.content}

if __name__ == "__main__":
    # serve_playground_app("main:app", reload=True)

    
    
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

# import os
# import agentops

# from agno.agent import Agent, RunResponse

# from dotenv import load_dotenv

# from tools.duckduckgo import agentWithTools
# from tools.youtube_tools import youtubeTools
# # Load environment variables from .env file
# load_dotenv()
# api_key = os.getenv("AGENTOPS_API_KEY")

# agentops.init()


# # agent = Agent(
# #     model=Groq(id="llama-3.1-8b-instant"),
# #     markdown=True
# # )

# # # Print the response in the terminal
# # agent.print_response("Share a 2 sentence horror story.")

# # agentWithTools()

# youtubeTools()

# agentops.end_session('Success')
