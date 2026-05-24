"""
Pandas analyzer module.

Laboratory work №4.
Task 6, variant 11.

Dataset: FIFA 19.
"""

import pandas as pd


class BasePandasAnalyzer:
    """Base class for pandas analyzers."""

    def analyze(self):
        """Analyze dataset."""
        raise NotImplementedError


class FifaAnalyzer(BasePandasAnalyzer):
    """Class for analyzing FIFA 19 dataset."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

    @staticmethod
    def convert_wage_to_number(value) -> float:
        """Convert FIFA wage format to numeric value."""

        if pd.isna(value):
            return 0.0

        value = str(value).replace("€", "").strip()

        if value.endswith("K"):
            return float(value[:-1]) * 1000

        if value.endswith("M"):
            return float(value[:-1]) * 1000000

        try:
            return float(value)
        except ValueError:
            return 0.0

    def create_player_sample(self) -> pd.DataFrame:
        """Create sample of 5 random players."""

        return (
            self.data[["Name", "Age", "Overall"]]
            .sample(5, random_state=42)
            .reset_index(drop=True)
        )

    def average_sprint_speed_below_average_wage(self) -> float:
        """Calculate average SprintSpeed for players whose Wage is below average."""

        data_copy = self.data.copy()

        data_copy["WageNumeric"] = data_copy["Wage"].apply(
            self.convert_wage_to_number
        )

        average_wage = data_copy["WageNumeric"].mean()

        filtered_players = data_copy[
            data_copy["WageNumeric"] < average_wage
        ]

        return round(filtered_players["SprintSpeed"].mean(), 2)

    def shot_power_ratio_by_aggression(self) -> float:
        """
        Calculate how many times average ShotPower of the most aggressive players
        is greater than average ShotPower of the least aggressive players.
        """

        max_aggression = self.data["Aggression"].max()
        min_aggression = self.data["Aggression"].min()

        max_group_mean = self.data[
            self.data["Aggression"] == max_aggression
        ]["ShotPower"].mean()

        min_group_mean = self.data[
            self.data["Aggression"] == min_aggression
        ]["ShotPower"].mean()

        if min_group_mean == 0:
            return 0.0

        return round(max_group_mean / min_group_mean, 2)

    def dataset_info(self) -> dict:
        """Return basic dataset information."""

        return {
            "rows": self.data.shape[0],
            "columns": self.data.shape[1],
            "column_names": list(self.data.columns)
        }

    def analyze(self) -> dict:
        """Perform full FIFA dataset analysis."""

        return {
            "dataset_info": self.dataset_info(),
            "player_sample": self.create_player_sample(),
            "average_sprint_speed_below_average_wage":
                self.average_sprint_speed_below_average_wage(),
            "shot_power_ratio_by_aggression":
                self.shot_power_ratio_by_aggression()
        }