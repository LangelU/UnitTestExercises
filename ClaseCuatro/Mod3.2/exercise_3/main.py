# Ejercicio 3 (Avanzado):
# En un sistema de carrito de compras, se tienen varias dependencias como
# servicios de pago y de inventario. Utiliza unittest.mock para simular estas
# dependencias y prueba que el proceso de compra maneje correctamente las
# interacciones con esas dependencias simuladas, verificando los resultados de
# la transacción

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def getCart(self):
        """
        Obtener el carrito.

        Returns:
            array: Lista de archivos almacenados.
        """
        return self.cart

    def addProduct(self, product):
        """
        Añade un producto al carrito.

        Args:
            product (array): Array clave/valor. Debe incluir el id del
            producto, el nombre, la cantidad y el costo.

        Returns:
            None
        """
        if (
            (product['id'] is None)
        ):
            return "Invalid key or value"
        key = product['id']
        productData = {
            "name": product['name'],
            "quantity": product['quantity'],
            "price": product['price']
        }
        self.cart[key] = productData

    def deleteProduct(self, productId):
        product = self.cart.get(productId)
        if product is None:
            return "Product not found"
        del self.cart[productId]

    def validateCart(self, userBalance):
        cart = self.cart
        if cart is None:
            return "Shopping cart empty"
        totalValue = 0
        for key, product in cart.items():
            value = product['price'] * product['quantity']
            totalValue = totalValue + value
        if userBalance >= totalValue:
            cart = self.cart = {}
            return {
                "message": "Cart procesed",
                "total_value": totalValue,
                "cart": cart,
                "user_original_balance": userBalance,
                "user_remaining_balance": userBalance - totalValue
            }
        return {
            "message": "Cart not procesed",
            "total_value": totalValue,
            "cart": cart,
            "user_original_balance": userBalance,
            "user_remaining_balance": userBalance - totalValue
        }

    def rechargeDependency(self):
        pass

    def billPaymentDependency(self):
        pass

    def inventoryServiceDependency(self):
        pass

    def makeupStoreDependency(self):
        pass

    def perfumeryStoreDependency(self):
        pass
