"""
Repository module for saving and loading synonym pairs.
"""

import csv
import pickle
from pathlib import Path

from task1_synonyms.models import ExtendedWordPair


class BaseRepository:
    """Base repository class."""

    def save(self, pairs: list[ExtendedWordPair], file_path: Path) -> None:
        """Save synonym pairs."""
        raise NotImplementedError

    def load(self, file_path: Path) -> list[ExtendedWordPair]:
        """Load synonym pairs."""
        raise NotImplementedError


class CsvSynonymRepository(BaseRepository):
    """Repository for CSV serialization."""

    def save(self, pairs: list[ExtendedWordPair], file_path: Path) -> None:
        """Save synonym pairs to CSV file."""
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["first_word", "second_word", "description"])

            for pair in pairs:
                writer.writerow([pair.first_word, pair.second_word, pair.description])

    def load(self, file_path: Path) -> list[ExtendedWordPair]:
        """Load synonym pairs from CSV file."""
        pairs = []

        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                pairs.append(
                    ExtendedWordPair(
                        row["first_word"],
                        row["second_word"],
                        row.get("description", "Synonym pair")
                    )
                )

        return pairs


class PickleSynonymRepository(BaseRepository):
    """Repository for pickle serialization."""

    def save(self, pairs: list[ExtendedWordPair], file_path: Path) -> None:
        """Save synonym pairs to pickle file."""
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "wb") as file:
            pickle.dump(pairs, file)

    def load(self, file_path: Path) -> list[ExtendedWordPair]:
        """Load synonym pairs from pickle file."""
        with open(file_path, "rb") as file:
            return pickle.load(file)