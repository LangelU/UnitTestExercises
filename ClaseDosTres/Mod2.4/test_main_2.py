import pytest
import main


@pytest.mark.parametrize("productPrice, discount, expected_value", [
    (100, 0, 100),      # Caso 1
    (100, 10, 90),     # Caso 2
    (100, 50, 40),   # Caso 3
])
def test_calculate_triangle_area(productPrice, discount, expected_value):
    assert main.calculateProductPrice(productPrice, discount) == expected_value
