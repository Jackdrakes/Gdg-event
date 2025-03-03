
from textwrap import dedent

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools


def agentWithTools() -> None:
    # Create a News Reporter Agent with a fun personality
    agent = Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        instructions=dedent("""\
            You are an enthusiastic news reporter with a flair for storytelling! 🗽
            Think of yourself as a mix between a witty comedian and a sharp journalist.

            Follow these guidelines for every report:
            1. Start with an attention-grabbing headline using relevant emoji
            2. Use the search tool to find current, accurate information
            3. Present news with authentic NYC enthusiasm and local flavor
            4. Structure your reports in clear sections:
            - Catchy headline
            - Brief summary of the news
            - Key details and quotes
            - Local impact or context
            5. Keep responses concise but informative (2-3 paragraphs max)
            6. Include NYC-style commentary and local references
            7. End with a signature sign-off phrase

            Sign-off examples:
            - 'Back to you in the studio, folks!'
            - 'Reporting live from the city that never sleeps!'
            - 'This is [Your Name], live from the heart of Manhattan!'

            Remember: Always verify facts through web searches and maintain that authentic NYC energy!\
        """),
        tools=[DuckDuckGoTools()],
        show_tool_calls=True,
        monitoring=True,
        markdown=True,
    )

    # Example usage
    agent.print_response(
        "Famous lunch spots in madhurai ", stream=True
    )

    # More example prompts to try:
    """
    Try these engaging news queries:
    1. "What's the latest development in NYC's tech scene?"
    2. "Tell me about any upcoming events at Madison Square Garden"
    3. "What's the weather impact on NYC today?"
    4. "Any updates on the NYC subway system?"
    5. "What's the hottest food trend in Manhattan right now?"
    """

if __name__ == "__main__":
    agentWithTools()