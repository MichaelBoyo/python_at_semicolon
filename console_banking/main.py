from console_banking.account import Account
from console_banking.bank import Bank
from console_banking.customer import Customer
from console_banking.sign_in import sign_in
from console_banking.sign_up import sign_up

print("WELCOME TO PYTHON BANK")
sentinel = 0

bank = Bank()


def delete_profile():
    email = input("enter email: ")
    customer_to_delete = bank.get_a_customer(email)
    bank.remove_customer(customer_to_delete)
    print("delete success")
    pass


while sentinel != -1:
    prompt = """"
    1 -> SignUp
    2 -> SignIn to existing Account
    3 -> view all Customers
    4 -> delete profile
    0 -> End 
    """
    print(prompt)
    user_input = int(input(""))
    match user_input:
        case 1:
            sign_up(bank)
        case 2:
            sign_in(bank)
        case 3:
            all_customers = bank.get_all_customers()
            for customer in all_customers:
                print(customer)
        case 4:
            delete_profile()
        case 0:
            sentinel = -1
