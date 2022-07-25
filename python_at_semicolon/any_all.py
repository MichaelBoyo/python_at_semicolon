# lst = [1, 0, 5, 6, 7, 8]
# print(any(i for i in lst if i >= 7))
# print(all(lst))
# print(all(True if i >= 7 else False for i in lst))
# lst = ["koko", "boyo", "moyo", "dodo"]
# lst2 = ["moko", "poko", "jojo"]
# print(list(zip(lst, lst2)))
a_score = [[89, 66, 66], [56, 78, 99], [90, 89, 88]]

max(sum(l) for l in a_score)
date_ = [{"name": "abu",
          "scores": [23, 55, 66]},
         {"name": "john",
          "scores": [93, 67, 79]},
         {"name": "abu",
          "scores": [89, 77, 89]}]
# print(max(sum(l["scores"]) for l in date_))

#
# def get(lst: list):
#     for a in lst:
#         b = a
#         lst.remove(a)
#         return b
#
#
numb = [1, 4, 5, 6, 6]
mapped = list(map(lambda x: x ** 2, numb))
# print(mapped)
lis_ = [{"name": "asake", "gender": "F"}, {"name": "Boyo", "gender": "M"}]
map___ = [("Mr. " if x["gender"] == "M" else "Mrs. ") + x["name"] for x in lis_]
map____ = ["Mr. " + x["name"] for x in lis_ if x["gender"] == "M"]
map__ = list(map(lambda x: ("Mr. " if x["gender"] == "M" else "Mrs. ") + x["name"], lis_))
fil_ = filter(lambda x: x["gender"] == "M", lis_)
print("kk")
print(fil_)
print("kk")

from functools import reduce
import operator

red_ = reduce(lambda acc, val: acc + val, numb, 100)
red__ = reduce(operator.add, numb, 100)
fruits = ["apple", "cucumber", "banana", "water-melon"]
# print(reduce(lambda x, y: x if len(x) > len(y) else y, fruits))
# print(reduce(lambda x, y: x if len(x) >= len(y) else y, fruits))

# let = 7
# def main_1():

# print(red_)
# print(red__)
# # position = []
# # b = len(a_score)
# # for i in range(b):
# # str_ = max(dict_, key=lambda a: sum(a for a in get(a_score)))
# str_ = max(dict_, key=lambda a: sum(a for a in a_score))
# print(type(str_))
# new_dct_ = {str_: }
# position.append(new_dct_)
#     # for a in dict_:
#     #     if a == str_:
#     #         dict_.pop(a)
#
# for p in position:
#     print(p)
