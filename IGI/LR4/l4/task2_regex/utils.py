"""
Utility functions for text processing.
"""

import re


def load_text(file_path: str) -> str:
    """Load text from file."""

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def save_text(file_path: str, content: str) -> None:
    """Save text to file."""

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def extract_words(text: str) -> list[str]:
    """Extract words from text."""

    return re.findall(r"\b[\w']+\b", text)