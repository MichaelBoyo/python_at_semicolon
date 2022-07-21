import doctest


def add(a, b):
    """
    >>> add(3,5)
    8
    >>> add(2,"hi")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


# def flip(lst: list):
#     """"
#     >>> flip([1,3,7,9])
#     9
#     """
#     return lst[-1]


# if __name__ == '__main__':
#     doctest.testmod()

