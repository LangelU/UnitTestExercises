import unittest
import main


class TestGerLargestNumber(unittest.TestCase):
    def test_get_largest(self):
        list = [1, 2, 9, 4, 6, 7, 8]
        expected_value = 9
        result = main.getlargestNumberOfAList(list)
        self.assertEqual(result, expected_value)

    def test_empty_list(self):
        list = []
        expected_value = None
        result = main.getlargestNumberOfAList(list)
        self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main()
