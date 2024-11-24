import unittest
from unittest.mock import MagicMock
from main import SumNumbers


class TestSumNumbers(unittest.TestCase):
    def test_successfull_sum_numbers(self):
        """
            Esta prueba verifica la correcta
            sumatoria de una lista de números
        """
        service = SumNumbers()
        service.numbersList = MagicMock(return_value=[1, 2, 3, 4, 5])
        mock = service.numbersList()
        result = service.sumNumbersOfList(mock)
        expected_value = 16
        self.assertEqual(result, expected_value)

    def test_failed_sum_numbers(self):
        """
            Esta prueba verifica la incorrecta
            sumatoria de una lista de números
        """
        service = SumNumbers()
        service.numbersList = MagicMock(return_value=[1, 2, 3, 4, 5])
        mock = service.numbersList()
        result = service.sumNumbersOfList(mock)
        expected_value = 20
        self.assertNotEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main()
