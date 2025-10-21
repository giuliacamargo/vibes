"""Command-line interface for Reddit Thread Summarizer."""

import sys
import click
from .fetcher import RedditFetcher
from .summarizer import ThreadSummarizer


@click.group()
@click.version_option(version='1.0.0')
def cli():
    """Reddit Thread Summarizer - Summarize Reddit threads using AI."""
    pass


@cli.command()
@click.argument('url')
@click.option(
    '--type', '-t',
    type=click.Choice(['comprehensive', 'brief', 'key_points'], case_sensitive=False),
    default='comprehensive',
    help='Type of summary to generate'
)
@click.option(
    '--max-comments', '-m',
    type=int,
    default=50,
    help='Maximum number of comments to include'
)
@click.option(
    '--show-thread', '-s',
    is_flag=True,
    help='Show the formatted thread text before summarizing'
)
def summarize(url, type, max_comments, show_thread):
    """Summarize a Reddit thread from URL."""
    try:
        click.echo("Fetching Reddit thread...")
        fetcher = RedditFetcher()
        thread_data = fetcher.fetch_thread(url)

        click.echo(f"✓ Fetched thread: {thread_data['title']}")
        click.echo(f"  Subreddit: r/{thread_data['subreddit']}")
        click.echo(f"  Comments: {thread_data['num_comments']}\n")

        thread_text = fetcher.format_thread_for_summary(thread_data, max_comments)

        if show_thread:
            click.echo("=" * 80)
            click.echo("FORMATTED THREAD TEXT")
            click.echo("=" * 80)
            click.echo(thread_text)
            click.echo("=" * 80 + "\n")

        click.echo("Generating summary with Claude AI...")
        summarizer = ThreadSummarizer()
        summary = summarizer.summarize(thread_text, summary_type=type)

        click.echo("\n" + "=" * 80)
        click.echo("SUMMARY")
        click.echo("=" * 80)
        click.echo(summary)
        click.echo("=" * 80)

    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('url')
@click.option(
    '--max-comments', '-m',
    type=int,
    default=50,
    help='Maximum number of comments to include'
)
def sentiment(url, max_comments):
    """Analyze sentiment of a Reddit thread."""
    try:
        click.echo("Fetching Reddit thread...")
        fetcher = RedditFetcher()
        thread_data = fetcher.fetch_thread(url)

        click.echo(f"✓ Fetched thread: {thread_data['title']}")
        click.echo(f"  Subreddit: r/{thread_data['subreddit']}")
        click.echo(f"  Comments: {thread_data['num_comments']}\n")

        thread_text = fetcher.format_thread_for_summary(thread_data, max_comments)

        click.echo("Analyzing sentiment with Claude AI...")
        summarizer = ThreadSummarizer()
        analysis = summarizer.analyze_sentiment(thread_text)

        click.echo("\n" + "=" * 80)
        click.echo("SENTIMENT ANALYSIS")
        click.echo("=" * 80)
        click.echo(analysis)
        click.echo("=" * 80)

    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('url')
@click.option(
    '--max-comments', '-m',
    type=int,
    default=50,
    help='Maximum number of comments to include'
)
def fetch(url, max_comments):
    """Fetch and display a Reddit thread without summarizing."""
    try:
        click.echo("Fetching Reddit thread...")
        fetcher = RedditFetcher()
        thread_data = fetcher.fetch_thread(url)

        click.echo(f"\n✓ Fetched thread: {thread_data['title']}")
        click.echo(f"  Author: u/{thread_data['author']}")
        click.echo(f"  Subreddit: r/{thread_data['subreddit']}")
        click.echo(f"  Score: {thread_data['score']}")
        click.echo(f"  Comments: {thread_data['num_comments']}\n")

        thread_text = fetcher.format_thread_for_summary(thread_data, max_comments)

        click.echo("=" * 80)
        click.echo(thread_text)
        click.echo("=" * 80)

    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == '__main__':
    main()
