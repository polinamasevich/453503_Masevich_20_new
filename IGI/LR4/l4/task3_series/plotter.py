"""
Plotter module for task 3.
"""

from pathlib import Path

import matplotlib.pyplot as plt


class SeriesPlotter:
    """Class for plotting series and math function values."""

    @staticmethod
    def plot(
        x_values: list[float],
        series_values: list[float],
        math_values: list[float],
        output_file: str
    ) -> None:
        """Build and save plot."""

        Path(output_file).parent.mkdir(parents=True, exist_ok=True)

        plt.figure(figsize=(10, 6))

        plt.plot(
            x_values,
            series_values,
            marker="o",
            color="blue",
            label="Series F(x)"
        )

        plt.plot(
            x_values,
            math_values,
            marker="s",
            color="red",
            label="Math F(x)"
        )

        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)

        plt.title("Comparison of series expansion and math function")
        plt.xlabel("x")
        plt.ylabel("F(x)")
        plt.legend()
        plt.grid(True)

        max_index = series_values.index(max(series_values))

        plt.annotate(
            "Max series value",
            xy=(x_values[max_index], series_values[max_index]),
            xytext=(x_values[max_index], series_values[max_index] + 0.1),
            arrowprops=dict(facecolor="black", shrink=0.05)
        )

        plt.savefig(output_file)
        plt.close()