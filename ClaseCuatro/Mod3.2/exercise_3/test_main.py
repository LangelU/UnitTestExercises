import unittest
from unittest.mock import MagicMock
from main import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def test_add_product_to_shopping_cart(self):
        """
            Esta prueba verifica la correcta adición de productos
            al carrito de compras
        """
        service = ShoppingCart()
        service.inventoryServiceDependency = MagicMock(return_value={
            "id": "ISD1",
            "name": "Servicio mensual de inventario",
            "quantity": 1,
            "price": 100
        })

        expected_value = {
            "ISD1": {
                "name": "Servicio mensual de inventario",
                "quantity": 1,
                "price": 100
            }
        }

        mock = service.inventoryServiceDependency()
        service.addProduct(mock)
        result = service.getCart()
        service.inventoryServiceDependency.assert_called_once()
        self.assertEqual(result, expected_value)

    def test_delete_product_from_shopping_cart(self):
        service = ShoppingCart()
        """
            Esta prueba verifica la correcta eliminación de un
            producto del carrito de compras
        """

        service.inventoryServiceDependency = MagicMock(return_value={
            "id": "ISD1",
            "name": "Servicio mensual de inventario",
            "quantity": 1,
            "price": 100
        })

        service.rechargeDependency = MagicMock(return_value={
            "id": "RCHD1",
            "name": "Recarga de saldo telefónico",
            "quantity": 1,
            "price": 200
        })

        """Añadir los items al carrito"""
        mock1 = service.inventoryServiceDependency()
        mock2 = service.rechargeDependency()
        service.addProduct(mock1)
        service.addProduct(mock2)

        service.deleteProduct("ISD1")
        result = service.getCart()

        expected_value = {
            "RCHD1": {
                "name": "Recarga de saldo telefónico",
                "quantity": 1,
                "price": 200
            }
        }

        service.inventoryServiceDependency.assert_called_once()
        service.rechargeDependency.assert_called_once()
        self.assertEqual(result, expected_value)

    def test_validate_shopping_cart(self):
        """
            Esta prueba verifica la correcta validación y
            procesamiento de un carrito de compras, validando
            que el cliente posea saldo suficiente para efectuar
            la transacción
        """
        service = ShoppingCart()
        service.inventoryServiceDependency = MagicMock(return_value={
            "id": "ISD1",
            "name": "Servicio mensual de inventario",
            "quantity": 1,
            "price": 100
        })

        service.rechargeDependency = MagicMock(return_value={
            "id": "RCHD1",
            "name": "Recarga de saldo telefónico",
            "quantity": 3,
            "price": 1200
        })

        service.perfumeryStoreDependency = MagicMock(return_value={
            "id": "PSTD1",
            "name": "Perfume uno",
            "quantity": 2,
            "price": 250
        })

        service.makeupStoreDependency = MagicMock(return_value={
            "id": "MKSTD1",
            "name": "Labial uno",
            "quantity": 4,
            "price": 325
        })

        user_balance = 10000
        expected_value = {
            "message": "Cart procesed",
            "total_value": 5500,
            "cart": {},
            "user_original_balance": user_balance,
            "user_remaining_balance": 4500
        }
        mock1 = service.inventoryServiceDependency()
        mock2 = service.rechargeDependency()
        mock3 = service.perfumeryStoreDependency()
        mock4 = service.makeupStoreDependency()

        service.addProduct(mock1)
        service.addProduct(mock2)
        service.addProduct(mock3)
        service.addProduct(mock4)
        result = service.validateCart(user_balance)
        service.inventoryServiceDependency.assert_called_once()
        service.rechargeDependency.assert_called_once()
        self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main()
