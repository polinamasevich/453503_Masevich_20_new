"""
Laboratory work №4.
Task 1: Working with CSV and pickle serializers.

Program version: 1.0
Developer: Polina
Development date: 2026

This module contains classes for storing synonym pairs.
"""


class PrintableMixin:
    """Mixin that adds formatted output behavior."""

    def to_pretty_string(self) -> str:
        """Return formatted object information."""
        return str(self)


class WordPair(PrintableMixin):
    """Class representing a pair of synonym words."""

    pair_count = 0

    def __init__(self, first_word: str, second_word: str):
        self.first_word = first_word
        self.second_word = second_word
        WordPair.pair_count += 1

    @property
    def first_word(self) -> str:
        """Get the first word."""
        return self.__first_word

    @first_word.setter
    def first_word(self, value: str) -> None:
        """Set the first word with validation."""
        if not value or not value.strip():
            raise ValueError("First word cannot be empty.")
        self.__first_word = value.strip().lower()

    @property
    def second_word(self) -> str:
        """Get the second word."""
        return self.__second_word

    @second_word.setter
    def second_word(self, value: str) -> None:
        """Set the second word with validation."""
        if not value or not value.strip():
            raise ValueError("Second word cannot be empty.")
        self.__second_word = value.strip().lower()

    def contains(self, word: str) -> bool:
        """Check whether the pair contains the given word."""
        return word.lower() in (self.first_word, self.second_word)

    def get_synonym(self, word: str) -> str | None:
        """Return synonym for the given word."""
        word = word.lower()

        if word == self.first_word:
            return self.second_word

        if word == self.second_word:
            return self.first_word

        return None

    def __str__(self) -> str:
        return f"{self.first_word} — {self.second_word}"

    def __repr__(self) -> str:
        return f"WordPair(first_word='{self.first_word}', second_word='{self.second_word}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, WordPair):
            return False

        return {self.first_word, self.second_word} == {other.first_word, other.second_word}


class ExtendedWordPair(WordPair):
    """Inherited class with additional description."""

    def __init__(self, first_word: str, second_word: str, description: str = "Synonym pair"):
        super().__init__(first_word, second_word)
        self.description = description

    def to_pretty_string(self) -> str:
        """Return extended pair information."""
        return "Pair: {}; description: {}".format(super().__str__(), self.description)