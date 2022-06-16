from console_banking.account import Account


class Customer:
    accounts = []

    def __init__(self, first_name, last_name, gender, email, phone_number, year_of_birth, month_of_birth,
                 day_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.year_of_birth = year_of_birth
        self.month_of_birth = month_of_birth
        self.day_of_birth = day_of_birth

    def __str__(self):
        data = """"
        First Name {}
        Last Name {}
        gender {}
        Email {}
        Phone {}
        Age {}
        """.format(self.get_first_name(), self.get_last_name(), self.get_gender(), self.email
                   , self.get_phone_number(), self.get_age())
        return data

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_gender(self):
        return self.gender

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_year_of_birth(self):
        return self.year_of_birth

    def get_month_of_birth(self):
        return self.month_of_birth

    def get_day_of_birth(self):
        return self.day_of_birth

    def get_age(self):
        age = 0
        return age

    def add_account(self, account: Account):
        self.accounts.append(account)

    def remove_account(self, account: Account):
        self.accounts.remove(account)

    def get_an_account(self, email: int):
        for account in self.accounts:
            if email == account.get_email():
                return account
        raise Exception("account not found")

    def get_all_accounts(self):
        return self.accounts
