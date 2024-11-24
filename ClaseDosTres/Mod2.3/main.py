def substract(num1, num2):
    """
        Restar un número de otro.

        Args:
            num1 (int o float): Número uno a restar.
            num2 (int o float): Número dos a restar.

        Returns:
            int o float: Saldo restante luego del retiro.
    """
    response = num1 - num2
    return response


def findLargest(num1, num2):
    """
        Determinar el mayor entre 2 números.

        Args:
            num1 (int o float): Número uno a comparar.
            num2 (int o float): Número dos a comparar.

        Returns:
            int o float: Saldo restante luego del retiro.
    """
    largestNumber = 0
    if num1 > num2:
        largestNumber = num1
    else:
        largestNumber = num2
    return largestNumber


def getlargestNumberOfAList(list=[]):
    """
        Determinar el mayor entre una lista de números.

        Args:
            list (array): Lista de números a procesar.

        Returns:
            int o float: El mayor número encontrado.
    """
    if not list:
        return None
    largestNumber = list[0]
    for number in list:
        if number > largestNumber:
            largestNumber = number
    return largestNumber
