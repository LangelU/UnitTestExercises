import datetime


def calculateAreaOfATriangle(base, height):
    """
    Calcula el área de un triángulo dada su base y altura.

    Args:
        base (int | float): Base del triángulo.
        heigth (int | float): Alto del triángulo.

    Returns:
        int | float: El área del triángulo.
    """
    res = (base * height) / 2
    return res


def calculateProductPrice(productPrice, discount):
    """
    Calcula el precio de un producto dado su valor y
    el porcentaje del descuento.

    Args:
        productPrice (int | float): Precio del producto.
        discount (int | float): Porcentaje del descuento.

    Returns:
        int | float: El valor con el descuento aplicado.
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


def validateIfIsAnAdult(birthDate, adultAge):
    """
    Calcula si una persona es mayor de edad dada su fecha
    de nacimiento y la edad en la que se considera un adulto.

    Args:
        birthDate (string): Fecha de nacimiento.
        adultAge (int): Edad en la que la persona se considera adulta.

    Returns:
        boolean: Si es mayor de edad o no.
    """
    currentDate = datetime.date.today()
    birthDateConverted = datetime.datetime.strptime(birthDate, "%d/%m/%Y")
    diff = currentDate.year - birthDateConverted.year
    if diff >= adultAge:
        return True
    else:
        return False
