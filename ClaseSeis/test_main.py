from main import Calculator
import pytest


class TestCalculator:

    @pytest.mark.parametrize("num1, num2, operator, expected_value", [
        (5, 5, "+", 10),  # pragma: no cover
        (6, 3, "+", 9),
        (5, -2, "+", 3)
    ])
    def test_sum(self, num1, num2, operator, expected_value):
        calculator = Calculator()
        assert calculator.calculator(num1, num2, operator) == expected_value

    @pytest.mark.parametrize("num1, num2, operator, expected_value", [
        (5, 5, "-", 0),  # pragma: no cover
        (10, 2, "-", 8),
        (10, -2, "-", 12)
    ])
    def test_substract(self, num1, num2, operator, expected_value):
        calculator = Calculator()
        assert calculator.calculator(num1, num2, operator) == expected_value

    @pytest.mark.parametrize("num1, num2, operator, expected_value", [
        (5, 5, "*", 25),  # pragma: no cover
        (10, 2, "*", 20),
        (6, -3, "*", -18)
    ])
    def test_multiply(self, num1, num2, operator, expected_value):
        calculator = Calculator()
        assert calculator.calculator(num1, num2, operator) == expected_value

    @pytest.mark.parametrize("num1, num2, operator, expected_value", [
        (10, 2, "/", 5),  # pragma: no cover
        (10, 0, "/", None),
        (10, -2, "/", -5)
    ])
    def test_division(self, num1, num2, operator, expected_value):
        calculator = Calculator()
        assert calculator.calculator(num1, num2, operator) == expected_value

    # pragma: no cover
    @pytest.mark.parametrize("num1, num2, operator, expected_value", [
        (10, 2, "^", 100),
        (5, 2, "^", 25),
        (6, 2, "^", 36)
    ])
    def test_power(self, num1, num2, operator, expected_value):
        calculator = Calculator()
        assert calculator.calculator(num1, num2, operator) == expected_value
    # fin de pragma
