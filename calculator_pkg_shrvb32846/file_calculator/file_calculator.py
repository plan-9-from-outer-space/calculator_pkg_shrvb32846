import time
from pathlib import Path
from tqdm import tqdm

# These two imports are identical, using two different methods to import the same class. 
# The first is a relative import, and the second is an absolute import. 
# You can use either one, but not both at the same time.

from ..calculator import Calculator                     # relative path
# from calculator_pkg_ex.calculator import Calculator   # absolute path

class FileCalculator (Calculator):
    def __init__(
        self,
        path: Path = Path(__file__).parent / "nums.csv",
        expected_lines: int = 3,
    ) -> None:
        self.path: Path = path
        self.expected_lines: int = 3

    def add_file(self) -> float | None:
        total: float = 0
        with open(self.path) as f:
            for line in tqdm(
                f, total=self.expected_lines, desc="Summing lines in file"
            ):
                time.sleep(2)
                total += float(line)
        return total
