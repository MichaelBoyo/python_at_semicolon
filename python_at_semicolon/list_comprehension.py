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

# def cube(num):
#     return num ** 3
#
#
# cubes = [cube(i) for i in range(1, 54)]
# print(cubes)

# print(rotate.is_prime(711))
# def is_prime(num):
#     import math
#     root = math.ceil(math.sqrt(num))
#     # divisor = (num // 2) + 1
#     for i in range(2, root):
#         if num % i == 0:
#             return False
#     return True

def prime_num(number):
    # returns true if a number is prime
    factors, i = 0, 1
    while i <= number:
        if number % i == 0:
            factors += 1
        i += 1
    if factors == 2:
        return True
    return False


primes = [i for i in range(1, 10) if prime_num(i)]
print(primes)
