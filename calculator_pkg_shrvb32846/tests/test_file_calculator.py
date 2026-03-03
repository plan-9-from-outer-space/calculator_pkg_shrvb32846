from calculator_pkg_shrvb32846 import FileCalculator


def test_file_calculator() -> None:
    assert FileCalculator().add_file() == 6, "Add File Failed"
