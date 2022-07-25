def add(a=0, b=0):
    return a * b


def sum_(*numbers):
    from statistics import mean
    return mean(numbers)


# print(sum_(68, 77, 56))

lst = [67, 99, 88, 77, 89]
set_ = {1, 57, 8, 8, 7}
print(sum_(*lst, *set_))


def add2(a, b, /, c):  # args before the slash "/" are non-positional prams, and cannot be initialized in args supply
    print(a, b, c)


def add3(a, b, *, c):  # args before the asterisk "*" compulsory keyword args
    print(a, b, c)


def add4(a, *args, b=0, **kwargs):
    print(a)
    print(args)
    print(b)
    print(kwargs)


add2(2, 4, c=4)
add3(2, 4, c=8)
add4(2, 4, 5, 6, b=6, v=6, i=9)
