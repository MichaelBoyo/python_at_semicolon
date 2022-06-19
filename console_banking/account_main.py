from console_banking.account import Account
from console_banking.current_account import Current_Account

my_account = Account("michael", "boyomichaelbidemi@gmail.com", "1234")
my_account2 = Account("michael", "boyomichaelbidemi@gmail.com", "1234")
my_account.deposit(1000)

my_current_account = Current_Account("mike", "mike@mail.com", "1234", 100000)
print(my_current_account.get_account_number())

my_current_account2 = Current_Account("mike", "mike@mail.com", "1234", 100000)
print(my_current_account2.get_account_number())
print(my_current_account2.get_balance())

try:
    my_account.withdraw(350, "1234")
except:
    print("an error occurred")
