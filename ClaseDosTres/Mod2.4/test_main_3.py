import pytest
import main


@pytest.mark.parametrize("birthDate, adultAge, expected_value", [
    ("26/08/2020", 18, True),      # Caso 1
    ("20/07/2000", 18, True),     # Caso 2
    ("01/04/2010", 18, False),   # Caso 3
])
def test_if_is_an_adult(birthDate, adultAge, expected_value):
    assert main.validateIfIsAnAdult(birthDate, adultAge) == expected_value
