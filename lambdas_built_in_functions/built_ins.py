import builtins
from functools import reduce

var = 8
print(isinstance(var, float))
lst = [2, 3, 4, 5, 0]
print(list(map(lambda x: x ** 2, lst)))
print(list(filter(lambda x: x < 2, lst)))
print(reduce(lambda x, y: x + y, lst, 10))
print(sum(lst, 10))

print(reduce(lambda x, y: x + y, lst, 10))
dict_ = {"name": 0, "age": 0, "tweets": 0, "followers": 0, "following": 0, "isVerified": True}
tweets = "likes, content, comment"
get_ = "no of tweets, no of verified users, verified users, average age of users, sum of all tweets, max tweets, " \
       "no tweets "
assignment = "create a list of twitter users"
do_ = "active users- have tweets"
