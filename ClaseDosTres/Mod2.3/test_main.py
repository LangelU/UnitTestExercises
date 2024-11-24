import unittest
import main


class TestSubstract(unittest.TestCase):
    def test_substract_two_numbers(self):
        val1 = 5
        val2 = 3
        expected_value = 2
        result = main.substract(val1, val2)
        self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main()
