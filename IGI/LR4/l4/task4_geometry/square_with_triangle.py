"""
Square with equilateral triangle module.

Variant 11:
Build a square with an equilateral triangle on one side.
"""

import math
from pathlib import Path

import matplotlib.pyplot as plt

from task4_geometry.color import FigureColor
from task4_geometry.shape import GeometricFigure


class DrawableMixin:
    """Mixin for drawable figures."""

    def save_to_file(self, output_file: str) -> None:
        """Save figure drawing to file."""
        self.draw(output_file)


class SquareWithTriangle(GeometricFigure, DrawableMixin):
    """Class representing a square with an equilateral triangle."""

    figure_name = "Square with equilateral triangle"

    def __init__(self, side: float, color: str, label: str):
        if side <= 0:
            raise ValueError("Side length must be positive.")

        self.side = side
        self.color = FigureColor(color)
        self.label = label

    @property
    def side(self) -> float:
        """Get side length."""
        return self.__side

    @side.setter
    def side(self, value: float) -> None:
        """Set side length."""
        if value <= 0:
            raise ValueError("Side length must be positive.")

        self.__side = value

    def square_area(self) -> float:
        """Calculate square area."""
        return self.side ** 2

    def triangle_area(self) -> float:
        """Calculate equilateral triangle area."""
        return (math.sqrt(3) / 4) * self.side ** 2

    def area(self) -> float:
        """Calculate total figure area."""
        return self.square_area() + self.triangle_area()

    def perimeter(self) -> float:
        """Calculate outer perimeter of the composite figure."""
        return 5 * self.side

    def get_info(self) -> str:
        """Return figure information."""
        return (
            "{}\n"
            "Side: {:.2f}\n"
            "Color: {}\n"
            "Square area: {:.2f}\n"
            "Triangle area: {:.2f}\n"
            "Total area: {:.2f}\n"
            "Perimeter: {:.2f}"
        ).format(
            self.get_figure_name(),
            self.side,
            self.color,
            self.square_area(),
            self.triangle_area(),
            self.area(),
            self.perimeter()
        )

    def draw(self, output_file: str) -> None:
        """Draw figure and save it to file."""

        Path(output_file).parent.mkdir(parents=True, exist_ok=True)

        a = self.side
        triangle_height = math.sqrt(3) / 2 * a

        square_x = [0, a, a, 0, 0]
        square_y = [0, 0, a, a, 0]

        triangle_x = [0, a, a / 2, 0]
        triangle_y = [a, a, a + triangle_height, a]

        plt.figure(figsize=(7, 7))

        plt.fill(square_x, square_y, color=str(self.color), alpha=0.6)
        plt.fill(triangle_x, triangle_y, color=str(self.color), alpha=0.85)

        plt.plot(square_x, square_y, color="black")
        plt.plot(triangle_x, triangle_y, color="black")

        plt.text(
            a / 2,
            a / 2,
            self.label,
            ha="center",
            va="center",
            fontsize=12
        )

        plt.title(self.get_figure_name())
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axis("equal")
        plt.grid(True, linestyle="--", alpha=0.6)

        plt.savefig(output_file)
        plt.show()
        plt.close()

    def __str__(self) -> str:
        return self.get_info()