class BankManagement:
    def __init__(self):
        self.currentBalance = 0

    def withdrawCash(self, ammount):
        """
        Retirar monto de la cuenta.

        Args:
            ammount (int o float): monto a retirar.

        Returns:
            int o float: Saldo restante luego del retiro.
        """
        if ammount > self.currentBalance:
            return "Insufficient balance"
        self.currentBalance -= ammount
        return self.currentBalance

    def depositMoney(self, ammount):
        """
        Depositar monto en la cuenta.

        Args:
            ammount (int o float): monto a depositar.

        Returns:
            int o float: Saldo actual luego del depósito.
        """
        self.currentBalance += ammount
        return self.currentBalance

    def accountBalance(self):
        """
        Consultar saldo actual en la cuenta

        Args:


        Returns:
            int o float: Saldo actual.
        """
        return self.currentBalance
