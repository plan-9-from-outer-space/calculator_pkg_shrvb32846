class Calculator:
    def __init__(self) -> None:
        print("Calculator initialized 3")  # noqa: T201

    def add(self, num1: float, num2: float) -> float:
        return num1 + num2

    def subtract(self, num1: float, num2: float) -> float:
        return num1 - num2

    def multiply(self, num1: float, num2: float) -> float:
        return num1 * num2

    def divide(self, num1: float, num2: float) -> float:
        return float(num1 / num2)
