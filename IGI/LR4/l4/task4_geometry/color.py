"""
Color module for geometric figures.
"""


class FigureColor:
    """Class for storing figure color."""

    def __init__(self, color: str):
        self.color = color

    @property
    def color(self) -> str:
        """Get figure color."""
        return self.__color

    @color.setter
    def color(self, value: str) -> None:
        """Set figure color."""
        if not value or not value.strip():
            raise ValueError("Color cannot be empty.")

        self.__color = value.strip().lower()

    def __str__(self) -> str:
        return self.color