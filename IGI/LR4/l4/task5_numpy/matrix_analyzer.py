"""
NumPy matrix analyzer module.

Laboratory work №4.
Task 5, variant 11.

Find all matrix elements whose absolute value is greater than B,
store them in array C and calculate median in two ways.
"""

import numpy as np


class BaseMatrixAnalyzer:
    """Base class for matrix analyzers."""

    def analyze(self):
        """Analyze matrix."""
        raise NotImplementedError


class MatrixAnalyzer(BaseMatrixAnalyzer):
    """Class for analyzing integer matrix."""

    def __init__(self, rows: int, columns: int, min_value: int, max_value: int):
        if rows <= 0 or columns <= 0:
            raise ValueError("Rows and columns must be positive.")

        if min_value > max_value:
            raise ValueError("Minimum value cannot be greater than maximum value.")

        self.rows = rows
        self.columns = columns
        self.min_value = min_value
        self.max_value = max_value
        self.matrix = np.random.randint(
            min_value,
            max_value + 1,
            size=(rows, columns)
        )

    def find_elements_by_abs(self, border: int) -> np.ndarray:
        """Find elements whose absolute value is greater than border."""

        return self.matrix[np.abs(self.matrix) > border]

    @staticmethod
    def median_numpy(array: np.ndarray) -> float | None:
        """Calculate median using NumPy."""

        if array.size == 0:
            return None

        return float(np.median(array))

    @staticmethod
    def median_manual(array: np.ndarray) -> float | None:
        """Calculate median manually."""

        if array.size == 0:
            return None

        sorted_array = np.sort(array)
        length = len(sorted_array)
        middle = length // 2

        if length % 2 == 1:
            return float(sorted_array[middle])

        return float((sorted_array[middle - 1] + sorted_array[middle]) / 2)

    def analyze(self, border: int) -> dict:
        """Analyze matrix according to variant 11."""

        array_c = self.find_elements_by_abs(border)

        return {
            "matrix": self.matrix,
            "border": border,
            "array_c": array_c,
            "count": array_c.size,
            "median_numpy": self.median_numpy(array_c),
            "median_manual": self.median_manual(array_c),
        }