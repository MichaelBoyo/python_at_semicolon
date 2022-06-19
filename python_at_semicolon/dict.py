database = []


def register_user():
    name = input("enter name: ")
    age = int(input("enter age: "))
    gender = input("enter gender: ")
    a_type = input("account type: ")
    balance = int(input("enter balance: "))
    data = {"name": name,
            "age": age,
            "gender": gender,
            "account type": a_type,
            "balance": balance}
    database.append(data)


for i in range(1, 3):
    register_user()
    print()
print(database)
names = [names["name"] for names in database]
avg_age = sum(age["age"] for age in database) / len(database)
savings_acct = [dict(name=n["name"]) for n in database if n["account type"] == "savings"]
print(names)
print(avg_age)
print(savings_acct)


def get_balance(dic):
    return dic["balance"]


print(sorted(database, key=get_balance, reverse=True))
print(database)



