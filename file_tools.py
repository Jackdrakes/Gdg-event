from pathlib import Path

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.file import FileTools

agent = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[FileTools(Path("tmp/file"))],
    save_response_to_file=True,
    show_tool_calls=True)

agent.print_response(
    "What is the most advanced LLM currently? Save the answer to a file.", markdown=True
)