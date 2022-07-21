def sum_num(num1: int, num2: int) -> int:
    """

    :param num1:
    :param num2:
    :return:
    """
    return num1 * num2


def operate(fn, x, y):
    return fn(x, y)


def subtract(a, b):
    return a - b


print(operate(subtract, 2, 4))
print(operate(sum_num, 3, 4))
print(operate(lambda x, y: x * y, 3, 4))

division = lambda a, b: a // b
print(division(3, 5))

s = "I love chukwudi".split()
print(max(s, key=lambda x: x[-1]))
print(min(s, key=lambda x: x[-1]))
number = [1, 3, 4]
print(max(number))
ages = [{'name': "ade", "age": 5}, {'name': "titi" "ade", "age": 10}]
print("gibberish")
print(max(ages, key=lambda x: x["age"]))
print(max(ages, key=lambda x: len(x["name"])))
print(sorted(ages, key=lambda x: len(x["name"]), reverse=True))
# print(sum_num.__name__)
# print(sum_num.__doc__)
# print(sum_num.__annotations__)
