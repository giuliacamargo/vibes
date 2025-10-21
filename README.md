# Reddit Thread Summarizer

A powerful CLI tool that fetches Reddit threads and generates AI-powered summaries using Claude AI. Perfect for quickly understanding lengthy Reddit discussions without reading through hundreds of comments.

## Features

- Fetch Reddit threads with all comments
- Generate comprehensive, brief, or key-point summaries
- Analyze sentiment and tone of discussions
- Support for customizable comment limits
- Clean, easy-to-use command-line interface
- Powered by Claude AI for high-quality summaries

## Prerequisites

- Python 3.8 or higher
- Reddit API credentials
- Anthropic API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd vibes
```

2. Install the package:
```bash
pip install -e .
```

Or install dependencies directly:
```bash
pip install -r requirements.txt
```

## Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Get Reddit API credentials:
   - Go to https://www.reddit.com/prefs/apps
   - Click "Create App" or "Create Another App"
   - Choose "script" as the app type
   - Note down your `client_id` and `client_secret`

3. Get Anthropic API key:
   - Sign up at https://console.anthropic.com/
   - Create an API key

4. Edit `.env` file with your credentials:
```env
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=reddit_summarizer/1.0
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## Usage

### Summarize a Thread

Generate a comprehensive summary:
```bash
reddit-summarizer summarize "https://www.reddit.com/r/python/comments/..."
```

Generate a brief summary:
```bash
reddit-summarizer summarize "URL" --type brief
```

Generate key points:
```bash
reddit-summarizer summarize "URL" --type key_points
```

Limit the number of comments:
```bash
reddit-summarizer summarize "URL" --max-comments 30
```

Show the formatted thread before summarizing:
```bash
reddit-summarizer summarize "URL" --show-thread
```

### Analyze Sentiment

Analyze the sentiment and tone of a discussion:
```bash
reddit-summarizer sentiment "https://www.reddit.com/r/python/comments/..."
```

### Fetch Thread

Fetch and display thread content without summarizing:
```bash
reddit-summarizer fetch "https://www.reddit.com/r/python/comments/..."
```

### Command Options

All commands support:
- `--max-comments, -m`: Maximum number of comments to include (default: 50)

Summary command supports:
- `--type, -t`: Summary type (comprehensive, brief, key_points)
- `--show-thread, -s`: Show formatted thread text before summarizing

## Examples

### Example 1: Quick Brief Summary
```bash
reddit-summarizer summarize "https://www.reddit.com/r/technology/comments/xyz" -t brief
```

### Example 2: Detailed Analysis with Sentiment
```bash
reddit-summarizer summarize "https://www.reddit.com/r/AskReddit/comments/xyz" -t comprehensive
reddit-summarizer sentiment "https://www.reddit.com/r/AskReddit/comments/xyz"
```

### Example 3: Focus on Top Comments Only
```bash
reddit-summarizer summarize "https://www.reddit.com/r/programming/comments/xyz" -m 20 -t key_points
```

## Project Structure

```
vibes/
├── reddit_summarizer/
│   ├── __init__.py          # Package initialization
│   ├── cli.py               # Command-line interface
│   ├── fetcher.py           # Reddit API integration
│   └── summarizer.py        # AI summarization logic
├── .env.example             # Environment variables template
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── requirements.txt        # Python dependencies
└── setup.py               # Package setup configuration
```

## How It Works

1. **Fetching**: Uses PRAW (Python Reddit API Wrapper) to fetch Reddit threads and comments
2. **Formatting**: Organizes the thread and top comments into a structured format
3. **Summarization**: Sends the formatted text to Claude AI for intelligent summarization
4. **Output**: Displays the summary in a clean, readable format

## Dependencies

- `praw`: Reddit API wrapper
- `anthropic`: Claude AI SDK
- `click`: CLI framework
- `python-dotenv`: Environment variable management

## Troubleshooting

### "ANTHROPIC_API_KEY not found"
Make sure you've created a `.env` file and added your API key.

### "Reddit API errors"
Verify your Reddit credentials are correct in the `.env` file.

### "Too many comments"
Try reducing the `--max-comments` value for very large threads.

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
