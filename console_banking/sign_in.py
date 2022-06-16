def deposit(account):
    amount = int(input("enter amount: "))
    account.deposit(amount)
    print("deposit successful")
    pass


def withdraw(account):
    amount = int(input("enter amount"))
    pin = input("enter pin")
    account.withdraw(amount, pin)
    print("withdraw successful")
    pass


def transfer(bank, account):
    amount = int(input("enter amount: "))
    account_no = int(input("enter account no: "))
    pin = input("enter your pin")
    out = bank.transfer(account, account_no, amount, pin)
    print(out)
    pass


def sign_in(bank):
    email = input("enter email: ")
    pin = input("enter pin: ")
    customer_to_log_in = bank.get_a_customer(email)
    account_to_use = customer_to_log_in.get_an_account(email)

    account_to_use.validate_pin(pin)
    sent = 0
    while sent != -1:
        login_menu = """"
        you are logged into acct: {}
        Hi, {}!
        Balance: {}
        1 -> Add Money+
        2 -> Withdraw-
        3 -> Transfer-
        4 -> TransactionHistory
        5 -> View All Accounts
        0 -> end
        """.format(account_to_use.get_account_number(), customer_to_log_in.get_first_name(),
                   account_to_use.get_balance())
        print(login_menu)
        # accounts = customer_to_log_in.get_all_accounts()
        # if accounts.len() < 2:
        #     print("6 -> create")
        choice = int(input(""))
        match choice:
            case 1:
                deposit(account_to_use)
            case 2:
                withdraw(account_to_use)
            case 3:
                transfer(bank, account_to_use)
            case 4:
                acct_no = int(input("enter ac no:"))

                history = account_to_use.get_transaction_history()
                for each_history in history:
                    print(each_history)
            case 5:
                accounts = customer_to_log_in.get_all_accounts()
                for ac in accounts:
                    if ac.get_email() == customer_to_log_in.get_email():
                        print(ac)
            case 0:
                sent = -1
    pass
