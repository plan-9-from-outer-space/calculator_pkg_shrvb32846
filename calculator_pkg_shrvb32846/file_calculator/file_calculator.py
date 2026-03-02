
# Section 1: built-in packages
import time
from pathlib import Path

# Section 2: external packages
# from tqdm import tqdm

# Section 3: internal packages
# These two imports are identical, using two different methods to import the same class. 
# The first is a relative import, and the second is an absolute import. 
# You can use either one, but not both at the same time.
from ..calculator import Calculator                     # relative path
# from calculator_pkg_ex.calculator import Calculator   # absolute path

class FileCalculator (Calculator):
    def __init__(
        self,
        # "nums.cvs" will not work at runtime, so we need to use the 
        #   Path class to construct the relative path to the file.
        path: Path = Path(__file__).parent / "nums.csv",
        # expected_lines: int = 3,
    ) -> None:
        self.path: Path = path
        # self.expected_lines: int = expected_lines # 3

    def add_file (self) -> float | None:
        total: float | None = None
        with open(self.path) as f:
            for line in f:
                if total is None:
                    total = float(line)
                else:
                    total += float(line)
        return total

    # def add_file(self) -> float | None:
    #     total: float = 0
    #     with open(self.path) as f:
    #         for line in tqdm(
    #             f, total=self.expected_lines, desc="Summing lines in file"
    #         ):
    #             time.sleep(2)
    #             total += float(line)
    #     return total
