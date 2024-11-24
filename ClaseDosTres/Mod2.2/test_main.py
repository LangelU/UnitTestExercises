# Ejercicio avanzado: Crea una función que calcule el precio de un artículo con
# descuento. El precio base es $100 y el descuento es un porcentaje entre 0 y
# 100. Escribe las pruebas unitarias utilizando el principio AAA para:
#     • Un descuento del 10%.
#     • Un descuento del 50%.
#     • Un descuento del 0%.

import unittest
import main


class TestCalculateProductPrice(unittest.TestCase):
    def test_discount_10_percent(self):
        productPrice = 100
        discountPercent = 10
        expected_value = 80
        result = main.calculateProductPrice(productPrice, discountPercent)
        self.assertEqual(result, expected_value)

    def test_discount_50_percent(self):
        productPrice = 100
        discountPercent = 50
        expected_value = 50
        result = main.calculateProductPrice(productPrice, discountPercent)
        self.assertEqual(result, expected_value)

    def test_discount_0_percent(self):
        productPrice = 100
        discountPercent = 0
        expected_value = 100
        result = main.calculateProductPrice(productPrice, discountPercent)
        self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main()
