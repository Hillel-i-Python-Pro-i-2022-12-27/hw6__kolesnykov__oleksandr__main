from pathlib import Path
from typing import Final


ROOT_PATH: Final[Path] = Path(__file__).parents[2]
INPUT_FILES_PATH: Final[Path] = ROOT_PATH.joinpath("files_input")
OUTPUT_FILES_PATH: Final[Path] = ROOT_PATH.joinpath("files_output")
