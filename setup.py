"""Setup script for Reddit Thread Summarizer."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="reddit-thread-summarizer",
    version="1.0.0",
    author="Reddit Summarizer Team",
    description="A tool to summarize Reddit threads using Claude AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "praw>=7.7.1",
        "python-dotenv>=1.0.0",
        "anthropic>=0.18.0",
        "click>=8.1.7",
        "flask>=3.0.0",
        "flask-cors>=4.0.0",
    ],
    package_data={
        "reddit_summarizer": [
            "web/templates/*.html",
            "web/static/css/*.css",
        ],
    },
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "reddit-summarizer=reddit_summarizer.cli:main",
            "reddit-summarizer-web=reddit_summarizer.web:run_app",
        ],
    },
)
