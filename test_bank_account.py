import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_initial_balance_positive(self):
        account = BankAccount(100)
        self.assertEqual(account.get_balance(), 100)

    def test_initial_balance_zero(self):
        account = BankAccount(0)
        self.assertEqual(account.get_balance(), 0)

    def test_initial_balance_negative(self):
        with self.assertRaises(ValueError):
            BankAccount(-100)

    def test_deposit_positive_amount(self):
        account = BankAccount(100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)

    def test_deposit_zero_amount(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.deposit(0)

    def test_deposit_negative_amount(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.deposit(-50)

    def test_withdraw_positive_amount(self):
        account = BankAccount(100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)

    def test_withdraw_zero_amount(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw(0)

    def test_withdraw_negative_amount(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw(-50)

    def test_withdraw_more_than_balance(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw(150)

    def test_get_balance(self):
        account = BankAccount(100)
        self.assertEqual(account.get_balance(), 100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)
        account.withdraw(75)
        self.assertEqual(account.get_balance(), 75)

if __name__ == '__main__':
    unittest.main()
