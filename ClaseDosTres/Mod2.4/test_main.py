import pytest
import main


@pytest.mark.parametrize("base, height, expected_area", [
    (2, 4, 4),      # Caso 1
    (6, 8, 24),     # Caso 2
    (10, 12, 60),   # Caso 3
])
def test_calculate_triangle_area(base, height, expected_area):
    assert main.calculateAreaOfATriangle(base, height) == expected_area
