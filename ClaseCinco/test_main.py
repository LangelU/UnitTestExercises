from main import Calculator


def test_calculator():
    calculator = Calculator()
    assert calculator.calculator(5, 5, "+") == 10
    assert calculator.calculator(10, 2, "/") == 5
    assert calculator.calculator(10, 0, "/") is None
    assert calculator.calculator(10, -2, "/") == -5
    assert calculator.calculator(10, 2, "-") == 8
    assert calculator.calculator(10, -2, "-") == 12
    assert calculator.calculator(10, 2, "*") == 20
    assert calculator.calculator(10, 2, "^") == 100
