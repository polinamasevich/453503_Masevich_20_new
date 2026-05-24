"""
Laboratory work №4.
Topic: Files, classes, serializers, regular expressions and standard libraries.

Program version: 1.0
Developer: Masevich Polina
Development date: 26.04.2026
"""

import pickle
from pathlib import Path
from typing import Callable

from task1_synonyms.models import ExtendedWordPair, WordPair
from task1_synonyms.repository import CsvSynonymRepository, PickleSynonymRepository
from task1_synonyms.service import SynonymService

from task2_regex.analyzer import RegexTextAnalyzer
from task2_regex.archiver import ZipArchiver
from task2_regex.utils import load_text, save_text

from task3_series.plotter import SeriesPlotter
from task3_series.series_calculator import LogarithmSeriesCalculator
from task3_series.statistics_service import SequenceStatistics

from task4_geometry.square_with_triangle import SquareWithTriangle

from task5_numpy.matrix_analyzer import MatrixAnalyzer

from task6_pandas.fifa_analyzer import FifaAnalyzer


DATA_DIR = Path("data")
OUTPUT_DIR = Path("output")

CSV_FILE = DATA_DIR / "synonyms.csv"
PICKLE_FILE = DATA_DIR / "synonyms.pkl"
INPUT_TEXT_FILE = DATA_DIR / "input_text.txt"
ANALYSIS_RESULT_FILE = OUTPUT_DIR / "analysis_result.txt"
ANALYSIS_ARCHIVE_FILE = OUTPUT_DIR / "analysis_result.zip"
TASK3_PLOT_FILE = OUTPUT_DIR / "task3_series_plot.png"
TASK4_FIGURE_FILE = OUTPUT_DIR / "task4_figure.png"
FIFA_FILE = DATA_DIR / "fifa19.csv"


def ensure_directories() -> None:
    """Create required project directories."""

    DATA_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)


def print_header(title: str) -> None:
    """Print formatted console header."""

    print(f"\n========== {title} ==========")


def input_non_empty_string(message: str) -> str:
    """Read non-empty string from keyboard."""

    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input error: value cannot be empty.")


def input_int(message: str) -> int:
    """Read integer value from keyboard."""

    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Input error: enter an integer number.")


def input_positive_float(message: str) -> float:
    """Read positive float value from keyboard."""

    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Input error: value must be positive.")

        except ValueError:
            print("Input error: enter a valid number.")


def create_default_pairs() -> list[ExtendedWordPair]:
    """Create default synonym dictionary."""

    return [
        ExtendedWordPair("big", "large", "Size synonym"),
        ExtendedWordPair("small", "little", "Size synonym"),
        ExtendedWordPair("fast", "quick", "Speed synonym"),
        ExtendedWordPair("smart", "clever", "Ability synonym"),
        ExtendedWordPair("happy", "glad", "Emotion synonym"),
        ExtendedWordPair("sad", "unhappy", "Emotion synonym"),
        ExtendedWordPair("begin", "start", "Action synonym"),
        ExtendedWordPair("end", "finish", "Action synonym"),
    ]


def show_task1_menu() -> None:
    """Display task 1 menu."""

    print_header("SYNONYM DICTIONARY")
    print("1. Save data to CSV and pickle")
    print("2. Load data from CSV")
    print("3. Load data from pickle")
    print("4. Show all synonym pairs")
    print("5. Find synonym by word")
    print("6. Find synonym for the last word")
    print("7. Show class statistics")
    print("0. Back")


def run_task1() -> None:
    """Run task 1."""

    pairs = create_default_pairs()
    service = SynonymService(pairs)

    csv_repository = CsvSynonymRepository()
    pickle_repository = PickleSynonymRepository()

    while True:
        show_task1_menu()
        choice = input("Choose menu item: ").strip()

        try:
            if choice == "1":
                csv_repository.save(pairs, CSV_FILE)
                pickle_repository.save(pairs, PICKLE_FILE)
                print("Data successfully saved.")

            elif choice == "2":
                pairs = csv_repository.load(CSV_FILE)
                service = SynonymService(pairs)
                print("Data successfully loaded from CSV.")

            elif choice == "3":
                pairs = pickle_repository.load(PICKLE_FILE)
                service = SynonymService(pairs)
                print("Data successfully loaded from pickle.")

            elif choice == "4":
                print("\nAll synonym pairs:")
                service.print_all_pairs()

            elif choice == "5":
                word = input_non_empty_string("Enter word: ")
                synonym = service.find_synonym(word)

                if synonym:
                    print(f"Synonym for '{word}': {synonym}")
                else:
                    print("Word was not found.")

            elif choice == "6":
                result = service.get_last_word_synonym()

                if result:
                    last_word, synonym = result
                    print(f"Last word: {last_word}")
                    print(f"Synonym: {synonym}")
                else:
                    print("Dictionary is empty.")

            elif choice == "7":
                print("Number of created word pairs:", WordPair.pair_count)

            elif choice == "0":
                break

            else:
                print("Input error: invalid menu item.")

        except FileNotFoundError:
            print("File was not found.")
        except PermissionError:
            print("Permission denied.")
        except ValueError as error:
            print("Value error:", error)
        except pickle.UnpicklingError:
            print("Pickle format error.")
        except Exception as error:
            print("Unexpected error:", error)


def run_task2() -> None:
    """Run task 2."""

    print_header("TASK 2")
    ensure_directories()

    try:
        text = load_text(str(INPUT_TEXT_FILE))
        analyzer = RegexTextAnalyzer(text)

        print("\nWords containing letters a-o and digits:")
        print(analyzer.words_with_a_to_o_and_digits())

        number = input("\nEnter six-digit number: ")

        if analyzer.is_valid_six_digit_number(number):
            print("Valid six-digit number.")
        else:
            print("Invalid number.")

        results = analyzer.full_analysis()

        print("\nQuoted words count:")
        print(results["quoted_words_count"])

        print("\nLetter statistics:")
        for letter, count in results["letter_statistics"].items():
            print(f"{letter} -> {count}")

        print("\nComma-separated phrases:")
        for phrase in results["comma_phrases"]:
            print(f"- {phrase}")

        print("\nSentence statistics:")
        for name, value in results["sentence_statistics"].items():
            print(f"{name} -> {value}")

        print("\nSmileys count:")
        print(results["smileys_count"])

        formatted_result = "\n".join(
            f"{key}:\n{value}\n"
            for key, value in results.items()
        )

        save_text(str(ANALYSIS_RESULT_FILE), formatted_result)
        ZipArchiver.archive_file(str(ANALYSIS_RESULT_FILE), str(ANALYSIS_ARCHIVE_FILE))

        print("\nAnalysis successfully saved.")
        print("\nArchive information:")

        for info in ZipArchiver.get_archive_info(str(ANALYSIS_ARCHIVE_FILE)):
            print(f"File: {info.filename}, Compressed size: {info.compress_size} bytes")

    except FileNotFoundError:
        print(f"Input file was not found: {INPUT_TEXT_FILE}")
    except PermissionError:
        print("Permission denied.")
    except Exception as error:
        print("Unexpected error:", error)


def run_task3() -> None:
    """Run task 3."""

    print_header("TASK 3")
    ensure_directories()

    print("Variant 11:")
    print("ln((x + 1) / (x - 1)) = 2 * (1/x + 1/(3x^3) + 1/(5x^5) + ...)")
    print("Condition: |x| > 1")

    calculator = LogarithmSeriesCalculator()

    x_values = [1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 3.0]
    eps = 0.0001

    series_values = []
    math_values = []

    print("\nTable:")
    print("{:<8} {:<8} {:<18} {:<18} {:<12}".format(
        "x", "n", "F(x)", "Math F(x)", "eps"
    ))

    for x in x_values:
        try:
            series_value, n = calculator.calculate(x, eps)
            math_value = calculator.calculate_math_value(x)

            series_values.append(series_value)
            math_values.append(math_value)

            print("{:<8} {:<8} {:<18.8f} {:<18.8f} {:<12}".format(
                x,
                n,
                series_value,
                math_value,
                eps
            ))

        except ValueError as error:
            print(f"x = {x}: {error}")

    statistics_service = SequenceStatistics(series_values)

    print("\nStatistics for series values:")
    for name, value in statistics_service.full_statistics().items():
        print(f"{name} -> {value}")

    SeriesPlotter.plot(
        x_values,
        series_values,
        math_values,
        str(TASK3_PLOT_FILE)
    )

    print(f"\nPlot saved to {TASK3_PLOT_FILE}")


def run_task4() -> None:
    """Run task 4."""

    print_header("TASK 4")
    ensure_directories()

    print("Variant 11:")
    print("Build a square with an equilateral triangle on one side.")

    try:
        side = input_positive_float("Enter side length a: ")
        color = input_non_empty_string("Enter figure color: ")
        label = input_non_empty_string("Enter figure label: ")

        figure = SquareWithTriangle(side, color, label)

        print("\nFigure information:")
        print(figure)

        figure.save_to_file(str(TASK4_FIGURE_FILE))

        print(f"\nFigure saved to {TASK4_FIGURE_FILE}")

    except ValueError as error:
        print("Value error:", error)
    except Exception as error:
        print("Unexpected error:", error)


def run_task5() -> None:
    """Run task 5."""

    print_header("TASK 5")

    print("Variant 11:")
    print("Find all elements whose absolute value is greater than B.")
    print("Store them in array C and calculate median in two ways.")

    try:
        rows = input_int("Enter number of rows n: ")
        columns = input_int("Enter number of columns m: ")
        min_value = input_int("Enter minimum random value: ")
        max_value = input_int("Enter maximum random value: ")
        border = input_int("Enter B: ")

        analyzer = MatrixAnalyzer(rows, columns, min_value, max_value)
        result = analyzer.analyze(border)

        print("\nMatrix A:")
        print(result["matrix"])

        print("\nShape of matrix A:")
        print(result["matrix"].shape)

        print(f"\nB = {result['border']}")

        print("\nArray C:")
        print(result["array_c"])

        print("\nNumber of elements in C:")
        print(result["count"])

        if result["count"] == 0:
            print("\nThere are no elements whose absolute value is greater than B.")
        else:
            print(f"\nMedian using NumPy -> {round(result['median_numpy'], 2)}")
            print(f"Median using manual formula -> {round(result['median_manual'], 2)}")

    except ValueError as error:
        print("Value error:", error)
    except Exception as error:
        print("Unexpected error:", error)


def run_task6() -> None:
    """Run task 6."""

    print_header("TASK 6")
    print("Variant 11: FIFA 19 dataset")

    try:
        analyzer = FifaAnalyzer(str(FIFA_FILE))
        result = analyzer.analyze()

        print("\nDataset information:")
        print(f"Rows -> {result['dataset_info']['rows']}")
        print(f"Columns -> {result['dataset_info']['columns']}")

        print("\nPlayer sample:")
        print(result["player_sample"])

        print("\nAverage SprintSpeed of players whose Wage is below average:")
        print(result["average_sprint_speed_below_average_wage"])

        print("\nShotPower ratio:")
        print(result["shot_power_ratio_by_aggression"])

    except FileNotFoundError:
        print("Dataset file was not found.")
        print(f"Put FIFA 19 dataset into {FIFA_FILE}")
    except KeyError as error:
        print("Column error:", error)
        print("Check that dataset contains required columns:")
        print("Name, Age, Overall, Wage, SprintSpeed, Aggression, ShotPower")
    except Exception as error:
        print("Unexpected error:", error)


def show_lab_menu() -> None:
    """Display laboratory menu."""

    print_header("LABORATORY WORK 4")
    print("1. Task 1 - Synonym dictionary")
    print("2. Task 2 - Regex text analysis")
    print("3. Task 3 - Series and matplotlib")
    print("4. Task 4 - Geometry figure")
    print("5. Task 5 - NumPy matrix")
    print("6. Task 6 - Pandas FIFA 19")
    print("0. Exit")


def run_lab() -> None:
    """Run laboratory work."""

    actions: dict[str, Callable[[], None]] = {
        "1": run_task1,
        "2": run_task2,
        "3": run_task3,
        "4": run_task4,
        "5": run_task5,
        "6": run_task6,
    }

    ensure_directories()

    while True:
        show_lab_menu()
        choice = input("Choose task: ").strip()

        if choice == "0":
            print("Program finished.")
            break

        action = actions.get(choice)

        if action is None:
            print("Input error: invalid menu item.")
            continue

        action()


if __name__ == "__main__":
    run_lab()