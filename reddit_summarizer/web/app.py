"""Flask web application for Reddit Thread Summarizer."""

import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from ..fetcher import RedditFetcher
from ..summarizer import ThreadSummarizer

app = Flask(__name__)
CORS(app)

# Configure Flask
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/summarize', methods=['POST'])
def summarize():
    """API endpoint to summarize a Reddit thread."""
    try:
        data = request.get_json()
        url = data.get('url')
        summary_type = data.get('type', 'comprehensive')
        max_comments = data.get('max_comments', 50)

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        # Fetch thread
        fetcher = RedditFetcher()
        thread_data = fetcher.fetch_thread(url)

        # Format for summarization
        thread_text = fetcher.format_thread_for_summary(thread_data, max_comments)

        # Generate summary
        summarizer = ThreadSummarizer()
        summary = summarizer.summarize(thread_text, summary_type=summary_type)

        return jsonify({
            'success': True,
            'summary': summary,
            'thread_info': {
                'title': thread_data['title'],
                'author': thread_data['author'],
                'subreddit': thread_data['subreddit'],
                'score': thread_data['score'],
                'num_comments': thread_data['num_comments']
            }
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/sentiment', methods=['POST'])
def sentiment():
    """API endpoint to analyze sentiment of a Reddit thread."""
    try:
        data = request.get_json()
        url = data.get('url')
        max_comments = data.get('max_comments', 50)

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        # Fetch thread
        fetcher = RedditFetcher()
        thread_data = fetcher.fetch_thread(url)

        # Format for analysis
        thread_text = fetcher.format_thread_for_summary(thread_data, max_comments)

        # Analyze sentiment
        summarizer = ThreadSummarizer()
        analysis = summarizer.analyze_sentiment(thread_text)

        return jsonify({
            'success': True,
            'analysis': analysis,
            'thread_info': {
                'title': thread_data['title'],
                'author': thread_data['author'],
                'subreddit': thread_data['subreddit'],
                'score': thread_data['score'],
                'num_comments': thread_data['num_comments']
            }
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/fetch', methods=['POST'])
def fetch():
    """API endpoint to fetch a Reddit thread without summarizing."""
    try:
        data = request.get_json()
        url = data.get('url')
        max_comments = data.get('max_comments', 50)

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        # Fetch thread
        fetcher = RedditFetcher()
        thread_data = fetcher.fetch_thread(url)

        # Format thread
        thread_text = fetcher.format_thread_for_summary(thread_data, max_comments)

        return jsonify({
            'success': True,
            'thread_text': thread_text,
            'thread_info': {
                'title': thread_data['title'],
                'author': thread_data['author'],
                'subreddit': thread_data['subreddit'],
                'score': thread_data['score'],
                'num_comments': thread_data['num_comments']
            }
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def run_app(host='0.0.0.0', port=5000, debug=False):
    """Run the Flask application."""
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    run_app(debug=True)
