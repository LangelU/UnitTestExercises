# Ejercicio 1 (Fácil):
# Crea una función llamada sumar_numeros que reciba una lista de números y los
# sume. Luego, crea un test donde utilices un mock para simular una función
# que devuelve la lista de números. Asegúrate de verificar que la función
# sumar_numeros retorna el valor correcto.
class SumNumbers:
    def sumNumbersOfList(self, list=[]):
        """
        Sumar los número de una lista dada.

        Args:
            list (array): lista de números a procesar.

        Returns:
            int o float: la sumatoria de los números.
        """
        if list is None:
            return None
        totalSum = 0
        for num in list:
            if not isinstance(num, int):
                return "Invalid number"
            totalSum = totalSum + num
        return totalSum

    def numbersList():
        """
        Simular el retorno de una lista de números.
        """
        pass
