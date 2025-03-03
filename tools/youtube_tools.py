from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools

def youtubeTools(video_url : str = "https://www.youtube.com/watch?v=wazHMMaiDEA" ):
    agent = Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        tools=[YouTubeTools()],
        show_tool_calls=True,
        monitoring=True,
        description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
    )

    agent.print_response(f"Summarize this video {video_url}", markdown=True)

if __name__ == "__main__":
    youtubeTools()