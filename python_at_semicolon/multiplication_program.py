import itertools
# print("MULTIPLICATION TABLE")
# for x in range(1, 13):
#     for i in range(1, 13):
#         print("{:3d}{:>3s}{:>3d}{:>4s}{:3d}".format(x, "*", i, "= ", x*i))
#     print()

# for x, i in itertools.product(range(1, 13), range(1, 13)):
#     print("{:3d}{:>3s}{:>3d}{:>4s}{:3d}".format(x, "*", i, "= ", x * i))
#     if i == 12:
#         print()

for x, i in itertools.product(range(1, 13), range(1, 13)):
    print("{0:3}{1:>3}{2:>3}{3:>4}{4:3}".format(x, "*", i, "= ", x * i))
    if i == 12:
        print()
