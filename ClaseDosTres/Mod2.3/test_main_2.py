import unittest
import main


class TestFindLargestNumber(unittest.TestCase):
    def test_find_largest_5_and_3(self):
        num1 = 5
        num2 = 3
        expected_value = 5
        result = main.findLargest(num1, num2)
        self.assertEqual(result, expected_value)

    def test_find_largest_2_and_7(self):
        num1 = 2
        num2 = 7
        expected_value = 7
        result = main.findLargest(num1, num2)
        self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main()
