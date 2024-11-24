
def calculateProductPrice(productPrice, discount):
    """
        Calcular el costo de un producto aplicando un porcentade de
        descuento.

        Args:
            productPrice (int o float): Valor neto del producto.
            discount (int o float): porcentaje de descuento a aplicar

        Returns:
            int o float: Costo del producto con el valor de descuento aplicado.
    """
    if (
        (productPrice is None or productPrice < 0)
        or
        (discount is None or discount < 0)
    ):
        return None
    if discount == 0:
        return productPrice
    discountPercentage = discount / 100
    productFinalValue = productPrice - (productPrice * discountPercentage)
    return productFinalValue
