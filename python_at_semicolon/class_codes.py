import random

random.seed(45)
# lst = []
# for i in range(0, 10):
#     lst.append(i)
#
rng = list(range(1, 100, 5))
# print(rng)
#
# rng.pop(4)
# print(rng)
# rng.append([6, 7, 8])
# print(rng)
# rng.extend([3, 5, 7])
# print(rng)
# rng.insert(1, "t")
# print(rng)
# rng.append(7)
# num = rng.count(7)
#
# print(num)
# rng[1] = 9
# rng.pop()
# non = rng.remove(41)
# print(non)
# print(rng)

# random.shuffle(rng)
# rng.sort(reverse=True)
# print(rng)
# print(random.choice(rng))

# fruits = ["apple", "cherry", "pineapple", "banana", "raspberry"]
# fruits.sort(key=len, reverse=True)
# print(fruits)
# prime = list(range(1,100,3))
# print(prime)
# for a in range(1, 100):
#     if a % 2:


bracket = "{{[()]}}}"
a, b, c, d, e, f = "{", "[", "(", "}", "]", ")"

bra_list = []
for a in bracket:
    bra_list.append(a)
i = 0
open_b = []
for g in bra_list:
    if g == a or g == b or g == c:
        open_b.append(a)

        # del bra_list[0]
        # del bra_list[-1]
#     bra_list.append(a)
# count = 0
# not_found = 0
# for b in bracket:
#     if b in bra_list:
#         bra_list.remove(b)
bra_list.remove(bra_list[1])
print(bra_list)

# tup = ("3", 3, 4, [6, 7, 9])
# tup[3].append(0)
# print(tup)
