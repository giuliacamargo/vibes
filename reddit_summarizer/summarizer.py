"""Thread summarization using Claude AI."""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


class ThreadSummarizer:
    """Summarizes Reddit threads using Claude AI."""

    def __init__(self):
        """Initialize Anthropic client."""
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        self.client = Anthropic(api_key=api_key)

    def summarize(self, thread_text: str, summary_type: str = "comprehensive") -> str:
        """
        Summarize a Reddit thread.

        Args:
            thread_text: Formatted thread text
            summary_type: Type of summary (comprehensive, brief, key_points)

        Returns:
            Summary text
        """
        prompts = {
            "comprehensive": """Provide a comprehensive summary of this Reddit thread. Include:
1. Main topic and context
2. Key points from the original post
3. Main themes and opinions from the comments
4. Notable insights or interesting perspectives
5. Overall sentiment and consensus (if any)""",

            "brief": """Provide a brief 2-3 paragraph summary of this Reddit thread,
covering the main topic and key takeaways from the discussion.""",

            "key_points": """Extract and list the key points from this Reddit thread as bullet points.
Focus on the most important information and insights."""
        }

        system_prompt = prompts.get(summary_type, prompts["comprehensive"])

        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            temperature=0.7,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": f"Here is the Reddit thread to summarize:\n\n{thread_text}"
                }
            ]
        )

        return message.content[0].text

    def analyze_sentiment(self, thread_text: str) -> str:
        """
        Analyze the sentiment of a Reddit thread.

        Args:
            thread_text: Formatted thread text

        Returns:
            Sentiment analysis
        """
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            temperature=0.5,
            system="""Analyze the overall sentiment and tone of this Reddit thread.
Consider both the original post and the comments. Provide:
1. Overall sentiment (positive, negative, neutral, mixed)
2. Main emotions expressed
3. Level of agreement/disagreement in the discussion
4. Tone of the conversation (friendly, heated, informative, etc.)""",
            messages=[
                {
                    "role": "user",
                    "content": f"Analyze this Reddit thread:\n\n{thread_text}"
                }
            ]
        )

        return message.content[0].text
