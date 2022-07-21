import json
from pathlib import Path
import random

my_db = Path.cwd() / "db.json"
my_db.touch()


def save_data(lst: list) -> None:
    with my_db.open(mode="w", encoding='utf-8') as file:
        return json.dump(lst, file, indent=4)


def fetch_data():
    with my_db.open(mode='r', encoding='utf-8') as file:
        return json.load(file)


database: list = fetch_data()


def all_users():
    for data in database:
        print(data)


def verified_users():
    print([i for i in database if i["is_verified"] == True])


def verify_user():
    user_id_ = input("enter user id")
    for data in database:
        if data["id"] == user_id_:
            data["is_verified"] = True

    save_data(database)


def find_user_by_email(email):
    for user__ in database:
        if user__["email"] == email:
            return user__


def delete_user():
    email = input("enter email: ")
    user__ = find_user_by_email(email)
    database.remove(user__)
    save_data(database)


def admin():
    admin_exit = 0
    while admin_exit != -1:
        u = int(
            input("1-> view all users\n2-> view verified users\n3-> verifyUSer\n4-> deleteUser\n0-> exit\n"))
        match u:
            case 1:
                all_users()
            case 2:
                verified_users()
            case 3:
                verify_user()
            case 4:
                delete_user()
            case _:
                admin_exit = -1


tweetId = 0


def tweet(user_log: dict):
    tweet_ = input("enter tweet: ")
    global tweetId
    tweetId += 1
    tw_ = {"id": tweetId, "content": tweet_, "likes": 0, "comments": 0}
    user_log["tweets"].append(tw_)
    print("sent successfully")


def view_your_tweets(user_log: dict):
    print(user_log["tweets"])


def view_trending_tweets():
    for d in database:
        print(d["tweets"])


def view_profile(user_log):
    user_f = find_user_by_id(user_log["id"])
    print(user_f)


def find_tweet(user_log: dict, tweet_id: int):
    user_gotten = find_user_by_id(user_log["id"])
    for tweet_ in user_gotten["tweets"]:
        if tweet_["id"] == tweet_id:
            return tweet_
    return None


def view_following_tweets(user_log):
    following_tweets = [a["tweets"] for a in user_log["following"]]
    sent_ = 0
    while sent_ != -1:
        for a in following_tweets:
            print(a)
    user_in = int(input("1-> like\n2->comment"))


def get_user(email: str, password: str):
    database_ = fetch_data()
    for _user_ in database_:
        if _user_["email"] == email and _user_["password"] == password:
            return _user_, "successful"
    return None, "failed"


def log_in():
    email, password = input("enter email: "), input("enter password: ")
    user_log, status = get_user(email, password)
    print("login " + status)
    user_page(status, user_log)


def follow_user(user_log):
    user_names = [(a["id"], a["email"]) for a in database if a["id"] != user_log["id"]]
    sent_ = 0
    while sent_ != -1:
        print(user_names)
        no = input("enter userid to follow user: ")
        user_2_follow = find_user_by_id(no)
        user_2_follow["followers"].append((user_log["id"], user_log["email"]))
        user_log["following"].append((user_2_follow["id"], user_2_follow["email"]))
        sent = int(input("enter 1 to add another user or 0 to end"))
        if sent == 0:
            sent_ = -1


def find_user_by_id(userid: str):
    return list(filter(lambda x: x['id'] == userid, database))[0]


def view_followers(user_log):
    print(user_log["followers"])


def view_following(user_log):
    print(user_log["following"])


def user_page(status, user_log):
    if status != "failed":
        sentinel = 0
        while sentinel != -1:
            input_in = int(
                input("1 -> view profile\n2-> follow_user\n3 -> tweet\n4 -> view your tweets\n5 -> view tweets of "
                      "following\n6 -> view trending tweets\n7-> view followers\n8-> view following\n0 -> log_out\n"))
            match input_in:
                case 1:
                    view_profile(user_log)
                case 2:
                    follow_user(user_log)
                case 3:
                    tweet(user_log)
                case 4:
                    view_your_tweets(user_log)
                case 5:
                    view_following_tweets(user_log)
                case 6:
                    view_trending_tweets()
                case 7:
                    view_followers(user_log)
                case 8:
                    view_following(user_log)
                case _:
                    sentinel = -1


def generate_random_id():
    import string
    abc = string.ascii_lowercase
    lst = [a for a in abc]
    random_num = random.randint(0, len(string.ascii_lowercase))
    return lst[random_num] + str(random.randint(10, 1010101))


def sign_up_():
    first_name, last_name = input("enter first name: "), input("enter last name: ")
    email, password = input("enter email: "), input("enter password: ")
    id_ = generate_random_id()
    user_data = dict(id=id_, first_name=first_name, last_name=last_name, email=email, password=password,
                     followers=[], following=[], is_verified=False, tweets=[])
    save_data(fetch_data().append(user_data))
    print("sign up successful")


def user():
    user_exit = 0
    while user_exit != -1:
        u = int(
            input("1-> Sign up\n2-> log in\n0-> exit\n"))
        match u:
            case 1:
                sign_up_()
            case 2:
                log_in()
            case _:
                user_exit = -1


exit_key = 0

while exit_key != -1:
    print(type(fetch_data()))
    user_ = int(
        input("1-> admin\n2-> user\n0-> exit\n"))
    match user_:
        case 1:
            admin()
        case 2:
            user()
        case _:
            exit_key = -1
