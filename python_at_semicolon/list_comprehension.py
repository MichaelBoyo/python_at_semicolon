import rotate


# lst = [i for i in range(1, 11)]
# print(lst)
#
# lst = [i ** 2 if i % 2 == 0 else i for i in range(1, 11)]
# print(lst)
# x = "even" if 4 % 2 == 0 else "odd"
# print(x)

# out = sum([int(input(f"enter Student %d score:" % i)) for i in range(1, 10)])
# print(out)

# pr = [i for i in range(3, 100) if rotate.is_prime(i)]
# print(pr)

def cube(num):
    return num ** 3


cubes = [cube(i) for i in range(1, 54)]
print(cubes)

# print(rotate.is_prime(711))
