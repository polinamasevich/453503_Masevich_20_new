"""
Series calculator module for laboratory work №4, task 3.

Variant 11:
ln((x + 1) / (x - 1)) = 2 * (1/x + 1/(3x^3) + 1/(5x^5) + ...), |x| > 1
"""

import math


class BaseSeriesCalculator:
    """Base class for series calculators."""

    def calculate(self, x: float, eps: float):
        """Calculate function value using series."""
        raise NotImplementedError


class LogarithmSeriesCalculator(BaseSeriesCalculator):
    """Calculator for logarithmic series."""

    def __init__(self):
        self.function_name = "ln((x + 1) / (x - 1))"

    @staticmethod
    def validate_x(x: float) -> None:
        """Validate x value."""
        if abs(x) <= 1:
            raise ValueError("For this series condition |x| > 1 must be true.")

    def calculate(self, x: float, eps: float = 0.0001) -> tuple[float, int]:
        """Calculate function value using series expansion."""
        self.validate_x(x)

        total = 0.0
        n = 0

        while True:
            term = 1 / ((2 * n + 1) * (x ** (2 * n + 1)))
            total += term

            if abs(term) < eps:
                break

            n += 1

        return 2 * total, n + 1

    def calculate_math_value(self, x: float) -> float:
        """Calculate function value using math module."""
        self.validate_x(x)

        return math.log((x + 1) / (x - 1))