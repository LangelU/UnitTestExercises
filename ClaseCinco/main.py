# Cobertura Básica de Funciones
# Escribe un conjunto de pruebas unitarias para la función de la calculadora.
# Usa pytest para ejecutar las pruebas y utiliza coverage.py para verificar
# que la cobertura de código sea del 100%.

class Calculator:
    def calculator(self, val1, val2, operation=""):
        """
        Opera 2 números.

        Args:
            val1 (int): Primer valor a operar
            val2 (int): Segundo valor a operar
            operation (string): Identificador de la operación
            a realizar

        Returns:
            int: Resultado de la operación de los 2 valores
        """
        if operation == "+":
            return val1 + val2
        if operation == "-":
            return val1 - val2
        if operation == "/":
            if val2 == 0:
                return None
            return val1 / val2
        if operation == "*":
            return val1 * val2
        if operation == "^":
            return val1 ** val2
