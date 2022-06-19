from datetime import datetime

from console_banking.account_types import Account_types
from console_banking.transaction_history import Transaction
from console_banking.transaction_types import Transaction_Types


class Account:
    uid = 1000
    transactions = []

    def __init__(self, account_name, email, pin):
        self.account_number = 0
        Account.uid += 1
        self.account_name = account_name
        self.email = email
        self.balance = 0
        self.account_number += Account.uid
        self.account_type = Account_types.savings_account
        self.pin = pin

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("invalid amount")
        self.balance += amount
        sender, receiver = "self", "self"
        deposit_transaction = Transaction("deposit", amount, datetime.now(), sender, receiver)
        self.transactions.append(deposit_transaction)

    def set_account_number(self, number):
        self.account_number = number

    def withdraw(self, amount: int, pin: str):
        if self.pin != pin:
            raise Exception("wrong pin")
        self.balance -= amount
        sender, receiver = "self", "self"
        withdraw_trans = Transaction("Withdraw", amount, datetime.now(), sender, receiver)
        self.transactions.append(withdraw_trans)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def get_account_name(self):
        return self.account_name

    def get_email(self):
        return self.email

    def validate_pin(self, pin):
        if self.pin != pin:
            raise Exception("wrong pin")
        return self.pin == pin

    def get_transaction_history(self):
        return self.transactions

    def receive_transfer_transaction(self, transfer: Transaction):
        self.transactions.append(transfer)

    def __str__(self):
        return "email: {}\nAccount name {}\nAccount " \
               "no {}\nbalance: {}".format(self.get_account_name(),
                                           self.get_email(), self.get_account_number(), self.get_balance())
