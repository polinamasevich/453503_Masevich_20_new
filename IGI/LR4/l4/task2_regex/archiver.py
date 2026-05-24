"""
Module for archiving analysis results.
"""

import zipfile
from pathlib import Path


class ZipArchiver:
    """Class for creating ZIP archives."""

    @staticmethod
    def archive_file(source_file: str, archive_file: str) -> None:
        """Archive file into ZIP."""

        with zipfile.ZipFile(archive_file, "w", zipfile.ZIP_DEFLATED) as archive:
            archive.write(source_file, arcname=Path(source_file).name)

    @staticmethod
    def get_archive_info(archive_file: str) -> list:
        """Return archive information."""

        with zipfile.ZipFile(archive_file, "r") as archive:
            return archive.infolist()