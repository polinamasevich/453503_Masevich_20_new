"""
Statistics service module.
"""

import statistics


class SequenceStatistics:
    """Class for calculating statistical parameters."""

    def __init__(self, values: list[float]):
        self.values = values

    def mean(self) -> float:
        """Calculate arithmetic mean."""
        return statistics.mean(self.values)

    def median(self) -> float:
        """Calculate median."""
        return statistics.median(self.values)

    def mode(self):
        """Calculate mode."""
        modes = statistics.multimode(self.values)
        if len(modes) == len(self.values):
            return "No mode"

        return [round(value, 6) for value in modes]

    def variance(self) -> float:
        """Calculate variance."""
        if len(self.values) < 2:
            return 0.0

        return statistics.variance(self.values)

    def standard_deviation(self) -> float:
        """Calculate standard deviation."""
        if len(self.values) < 2:
            return 0.0

        return statistics.stdev(self.values)

    def full_statistics(self) -> dict:
        """Return all statistical values."""
        return {
            "mean": round(self.mean(), 6),
            "median": round(self.median(), 6),
            "mode": self.mode(),
            "variance": round(self.variance(), 6),
            "standard_deviation": round(self.standard_deviation(), 6),
        }