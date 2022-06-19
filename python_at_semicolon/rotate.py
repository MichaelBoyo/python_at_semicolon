import math


def rotate_list(lst, num):
    rotated = []
    i = 0
    while i < num:
        a = lst.pop(0)
        rotated = lst
        rotated.append(a)
        i = i + 1
    return rotated


def prime(value):
    # prints prime numbers between 1 and the value given
    lst = []
    for a in range(1, value):
        if prime_num(a):
            lst.append(a)
    return lst


def fibonacci(num):
    b, c = 0, 1
    for a in range(0, num):
        print(b, end=" ")
        nth = b + c
        b = c
        c = nth


def product_of_list(lst):
    total = 1
    for a in lst:
        total *= a
    return total


def get_longest_string(lst):
    lst.sort(key=len, reverse=True)
    return lst[0]

#
# my_list = [1, 4, 5, 6, 67, 6]
# print("question 1: rotate a list => ", rotate_list(my_list, 19))
# print("question 2: prime numbers from 0 to 100 => ", prime(100))
# print("question 3: product of items in a list => ", product_of_list(my_list))
# print("question 4: Fibonacci sequence => ", end=" ")
# fibonacci(20)
# print()
#
# my_list3 = ["i", "love", "you", "my_baby_girl"]
# print("question 4: longest element in a list => ", get_longest_string(my_list3))
