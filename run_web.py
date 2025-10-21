#!/usr/bin/env python3
"""Run the web interface for Reddit Thread Summarizer."""

import os
import sys
from reddit_summarizer.web import run_app

if __name__ == '__main__':
    # Get configuration from environment or use defaults
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 'yes')

    print(f"Starting Reddit Thread Summarizer Web Interface...")
    print(f"Server: http://localhost:{port}")
    print(f"Debug mode: {debug}")
    print("\nPress Ctrl+C to stop the server")
    print("-" * 50)

    try:
        run_app(host=host, port=port, debug=debug)
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)
