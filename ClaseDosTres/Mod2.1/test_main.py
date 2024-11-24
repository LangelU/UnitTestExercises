import unittest
from main import BankManagement


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.bank = BankManagement()

    def test_get_balance(self):
        account_balance = self.bank.accountBalance()
        expected_value = 0
        self.assertEqual(account_balance, expected_value)

    def test_deposit(self):
        ammount = self.bank.depositMoney(100)
        expected_value = 100
        self.assertEqual(ammount, expected_value)

    def test_witdraw(self):
        ammount_to_deposit = self.bank.depositMoney(100)
        ammount = self.bank.withdrawCash(50)
        expected_value = 50
        self.assertEqual(ammount, expected_value)

    def test_withdraw_with_insufficient_balance(self):
        ammount_to_deposit = self.bank.depositMoney(100)
        ammount_to_withdraw = self.bank.withdrawCash(200)
        expected_value = "Insufficient balance"
        self.assertEqual(ammount_to_withdraw, expected_value)


if __name__ == "__main__":
    unittest.main()
