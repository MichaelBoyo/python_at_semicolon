from console_banking.account import Account
from console_banking.customer import Customer


def sign_up(bank):
    first_name = input("enter first Name: ")
    last_name = input("enter last Name: ")
    gender = input("enter gender: ")
    email = input("enter email: ")
    phone = input("enter phone: ")
    year = int(input("enter year of birth: "))
    month = int(input("enter month of birth: "))
    day = int(input("enter day of birth: "))
    new_customer = Customer(first_name, last_name, gender, email, phone, year, month, day)
    bank.add_customer(new_customer)
    pin = input("enter pin to activate account: ")
    account = Account(first_name, email, pin)
    new_customer.add_account(account)
    print("account created successfully")

    pass
