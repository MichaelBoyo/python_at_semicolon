from datetime import datetime

from console_banking.account import Account
from console_banking.customer import Customer
from console_banking.transaction_history import Transaction
from console_banking.transaction_types import Transaction_Types


def validate_amount(amount):
    if amount < 0:
        raise Exception("invalid amount")


def credit_account(account: Account, amount):
    validate_amount(amount)
    account.balance += amount


def debit_account(account: Account, amount):
    validate_amount(amount)
    account.balance -= amount


class Bank:
    customers = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def remove_customer(self, customer: Customer):
        self.customers.remove(customer)

    def get_all_customers(self):
        return self.customers

    def transfer(self, account: Account, account_number, amount, pin):
        account.validate_pin(pin)
        debit_account(account, amount)
        for customer in self.customers:
            accounts = customer.get_all_accounts()
            for account1 in accounts:
                if account_number == account1.get_account_number():
                    credit_account(account1, amount)
                    sender, receiver = account.get_account_number(), account1.get_account_number()
                    transfer_transaction = Transaction("Transfer", amount, datetime.now(), sender,
                                                       receiver)
                    account.receive_transfer_transaction(transfer_transaction)
                    account1.receive_transfer_transaction(transfer_transaction)
                    return "transfer success"

    def get_a_customer(self, email):
        for customer in self.customers:
            if email == customer.get_email():
                return customer
        raise Exception("customer not found")
