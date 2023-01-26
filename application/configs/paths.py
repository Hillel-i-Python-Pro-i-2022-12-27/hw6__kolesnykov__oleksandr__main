from pathlib import Path
from typing import Final


ROOT_PATH: Final[Path] = Path(__file__).parents[2]
APPLICATION_PATH: Final[Path] = ROOT_PATH.joinpath("application")
INPUT_FILES_PATH: Final[Path] = ROOT_PATH.joinpath("files_input")
OUTPUT_FILES_PATH: Final[Path] = ROOT_PATH.joinpath("files_output")
USEFUL_DATA_PATH: Final[Path] = INPUT_FILES_PATH.joinpath("useful_data.txt")
OUTPUT_DATA_PATH: Final[Path] = OUTPUT_FILES_PATH.joinpath("output_data.txt")
PATH_TO_CSV: Final[Path] = APPLICATION_PATH.joinpath("find_average").joinpath("people_data(extended).csv")
