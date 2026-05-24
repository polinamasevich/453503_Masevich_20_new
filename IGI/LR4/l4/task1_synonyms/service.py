"""
Service module for working with synonym pairs.
"""

from task1_synonyms.models import ExtendedWordPair


class SynonymService:
    """Service class containing business logic for synonyms."""

    def __init__(self, pairs: list[ExtendedWordPair]):
        self.pairs = pairs

    def find_synonym(self, word: str) -> str | None:
        """Find synonym for the given word."""
        for pair in self.pairs:
            synonym = pair.get_synonym(word)

            if synonym is not None:
                return synonym

        return None

    def get_last_word_synonym(self) -> tuple[str, str] | None:
        """Return synonym for the last word from the dictionary."""
        if not self.pairs:
            return None

        last_pair = self.pairs[-1]
        last_word = last_pair.second_word
        synonym = last_pair.get_synonym(last_word)

        return last_word, synonym

    def get_sorted_pairs(self) -> list[ExtendedWordPair]:
        """Return synonym pairs sorted alphabetically by the first word."""
        return sorted(self.pairs, key=lambda pair: pair.first_word)

    def print_all_pairs(self) -> None:
        """Print all synonym pairs."""
        for pair in self.get_sorted_pairs():
            print(pair.to_pretty_string())