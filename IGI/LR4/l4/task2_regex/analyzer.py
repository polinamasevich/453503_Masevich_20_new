"""
Text analyzer module using regular expressions.
"""

import re
from collections import Counter

from task2_regex.utils import extract_words


class BaseAnalyzer:
    """Abstract text analyzer."""

    def analyze(self, text: str):
        """Analyze text."""
        raise NotImplementedError


class RegexTextAnalyzer(BaseAnalyzer):
    """Regex analyzer implementation."""

    def __init__(self, text: str):
        self.text = text

    def words_with_a_to_o_and_digits(self) -> list[str]:
        """
        Find words containing:
        - at least one letter from a to o
        - at least one digit
        """

        words = re.findall(r"\b[A-Za-z0-9]+\b", self.text)

        result = []

        for word in words:

            has_letter = re.search(r"[a-oA-O]", word)
            has_digit = re.search(r"\d", word)

            if has_letter and has_digit:
                result.append(word)

        return result

    def is_valid_six_digit_number(self, value: str) -> bool:
        """
        Check whether string is a valid six-digit number
        without leading zeros.
        """

        return bool(re.fullmatch(r"[1-9]\d{5}", value))

    def count_quoted_words(self) -> int:
        """
        Count words inside quotation marks.
        """

        quoted_fragments = re.findall(r'"(.*?)"', self.text)

        count = 0

        for fragment in quoted_fragments:
            count += len(extract_words(fragment))

        return count

    def letter_statistics(self) -> dict:
        """
        Count occurrences of every letter.
        """

        letters = re.findall(
            r"[a-zA-Zа-яА-Я]",
            self.text.lower()
        )

        return dict(Counter(letters))

    def comma_phrases_sorted(self) -> list[str]:
        """
        Return comma-separated phrases sorted alphabetically.
        """

        cleaned_text = self.text.replace("\n", " ")

        phrases = [
            phrase.strip()
            for phrase in cleaned_text.split(",")
        ]

        phrases = [phrase for phrase in phrases if phrase]

        return sorted(phrases)

    def sentence_statistics(self) -> dict:
        """
        Calculate sentence statistics.
        """

        sentences = re.findall(
            r"[^.!?]+[.!?]",
            self.text
        )

        declarative = len(
            re.findall(r"[^!?]+\.", self.text)
        )

        interrogative = len(
            re.findall(r"[^.]+\?", self.text)
        )

        imperative = len(
            re.findall(r"[^.]+!", self.text)
        )

        words = extract_words(self.text)

        avg_word_length = (
            sum(len(word) for word in words) / len(words)
            if words else 0
        )


        avg_sentence_length = (
            sum(
                len("".join(extract_words(sentence)))
                for sentence in sentences
            ) / len(sentences)
            if sentences else 0
        )

        return {
            "total_sentences": len(sentences),
            "declarative": declarative,
            "interrogative": interrogative,
            "imperative": imperative,
            "average_word_length": round(avg_word_length, 2),
            "average_sentence_length": round(avg_sentence_length, 2)
        }

    def count_smileys(self) -> int:
        """
        Count smileys according to task rules.
        """

        pattern = r"[:;]-*[\(\)\[\]]+"

        matches = re.findall(pattern, self.text)

        valid_matches = []

        for smiley in matches:

            brackets = re.findall(
                r"[\(\)\[\]]",
                smiley
            )

            if len(set(brackets)) == 1:
                valid_matches.append(smiley)

        return len(valid_matches)

    def full_analysis(self) -> dict:
        """
        Perform complete text analysis.
        """

        return {

            "words_with_letters_and_digits":
                self.words_with_a_to_o_and_digits(),

            "quoted_words_count":
                self.count_quoted_words(),

            "letter_statistics":
                self.letter_statistics(),

            "comma_phrases":
                self.comma_phrases_sorted(),

            "sentence_statistics":
                self.sentence_statistics(),

            "smileys_count":
                self.count_smileys()
        }