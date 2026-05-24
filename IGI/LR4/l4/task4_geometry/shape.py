"""
Base shape module.
"""

from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    """Abstract base class for geometric figures."""

    figure_name = "Geometric figure"

    @abstractmethod
    def area(self) -> float:
        """Calculate figure area."""
        pass

    @classmethod
    def get_figure_name(cls) -> str:
        """Return figure name."""
        return cls.figure_name