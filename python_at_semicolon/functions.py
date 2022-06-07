import math

sq = math.sqrt(12)
print("{:.2f}".format(sq))


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    converts celsius to fahrenheit
    :param celsius: float
    :return: fahrenheit: float
    """
    return celsius * 1.8 + 32


print(celsius_to_fahrenheit(100))