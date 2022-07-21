import math
import os
import random
import re
import sys


def count_apples_and_oranges(p, q, r, ss, apples_, oranges_):
    o_count = 0
    a_count = 0
    for orange in oranges_:
        ab = ss + orange
        if p <= ab <= q:
            o_count += 1
    for apple in apples_:
        ab = r + apple
        if p <= ab <= q:
            a_count += 1
    print(o_count)
    print(a_count)

    # Write your code here


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    count_apples_and_oranges(s, t, a, b, apples, oranges)
