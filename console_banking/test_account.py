from unittest import TestCase

from console_banking.account import Account


class TestAccount(TestCase):
    account = Account("mike", "mike@gmail.com", "1234")

    def test_deposit(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.get_balance(), 1000)

    def test_set_account_number(self):
        self.account.set_account_number(200)
        self.assertEqual(self.account.get_account_number(), 200)

    def test_withdraw(self):
        self.account.deposit(2000)
        self.account.withdraw(1000, "1234")
        self.assertEqual(self.account.get_balance(), 1000)

    def test_get_balance(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.get_balance(), 1000)

    def test_get_account_number(self):
        self.assertEqual(self.account.get_account_number(), 1001)

    def test_get_account_name(self):

        self.assertEqual(self.account.get_account_name(), "mike")

    def test_get_email(self):
        self.assertEqual(self.account.get_email(), "mike@gmail.com")

    def test_validate_pin(self):
        self.assertTrue(self.account.validate_pin("1234"))

    def test_get_transaction_history(self):
        self.account.deposit(1000)
        self.assertIsNotNone(self.account.get_transaction_history())
        history = self.account.get_transaction_history()
        for h in history:
            print(h)
        self.assertEqual(self.account.get_transaction_history(), history)

    def test_receive_transfer_transaction(self):
        self.fail()
