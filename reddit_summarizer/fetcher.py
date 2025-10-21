"""Reddit thread fetcher using PRAW."""

import os
from typing import Dict, List
import praw
from dotenv import load_dotenv

load_dotenv()


class RedditFetcher:
    """Fetches Reddit threads and comments."""

    def __init__(self):
        """Initialize Reddit API client."""
        self.reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent=os.getenv('REDDIT_USER_AGENT', 'reddit_summarizer/1.0')
        )

    def fetch_thread(self, url: str) -> Dict:
        """
        Fetch a Reddit thread with its comments.

        Args:
            url: Reddit thread URL

        Returns:
            Dictionary containing thread data
        """
        submission = self.reddit.submission(url=url)

        # Expand all comments
        submission.comments.replace_more(limit=None)

        # Collect thread data
        thread_data = {
            'title': submission.title,
            'author': str(submission.author),
            'score': submission.score,
            'url': submission.url,
            'selftext': submission.selftext,
            'num_comments': submission.num_comments,
            'created_utc': submission.created_utc,
            'subreddit': str(submission.subreddit),
            'comments': []
        }

        # Collect top-level comments and their replies
        for comment in submission.comments.list():
            if hasattr(comment, 'body'):
                comment_data = {
                    'author': str(comment.author) if comment.author else '[deleted]',
                    'body': comment.body,
                    'score': comment.score,
                    'depth': comment.depth
                }
                thread_data['comments'].append(comment_data)

        return thread_data

    def format_thread_for_summary(self, thread_data: Dict, max_comments: int = 50) -> str:
        """
        Format thread data into text for summarization.

        Args:
            thread_data: Thread data from fetch_thread
            max_comments: Maximum number of comments to include

        Returns:
            Formatted text string
        """
        lines = [
            f"Title: {thread_data['title']}",
            f"Subreddit: r/{thread_data['subreddit']}",
            f"Author: u/{thread_data['author']}",
            f"Score: {thread_data['score']} | Comments: {thread_data['num_comments']}",
            "",
            "Post Content:",
            thread_data['selftext'] if thread_data['selftext'] else "[No text content]",
            "",
            f"Top {max_comments} Comments:",
            ""
        ]

        # Sort comments by score and take top N
        sorted_comments = sorted(
            thread_data['comments'],
            key=lambda x: x['score'],
            reverse=True
        )[:max_comments]

        for i, comment in enumerate(sorted_comments, 1):
            indent = "  " * comment['depth']
            lines.append(f"{i}. {indent}[{comment['score']}] u/{comment['author']}:")
            lines.append(f"{indent}{comment['body']}")
            lines.append("")

        return "\n".join(lines)
