import unittest
from unittest.mock import MagicMock
from main import Product


class TestProductClass(unittest.TestCase):
    def test_successfull_get_product_price(self):
        """
            Esta prueba verifica la correcta obtención
            del precio de un producto
        """
        service = Product()
        service.getProductPrice = MagicMock(return_value=250)
        result = service.getProductPrice()
        expected_value = 300
        self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main()
