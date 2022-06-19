from console_banking import account_types
from console_banking.account import Account
from console_banking.account_types import Account_types


class Current_Account(Account):
    uid = 2000

    def __init__(self, account_name, email, pin, initial_deposit):
        super().__init__(account_name, email, pin)
        Current_Account.uid += 1
        self.deposit(initial_deposit)
        self.set_account_number(Current_Account.uid)
        self.account_type = Account_types.current_account
