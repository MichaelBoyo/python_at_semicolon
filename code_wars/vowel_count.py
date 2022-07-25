def count(sentence):
    return sum(1 for let in sentence if let in "aeiouAEIOU")


def points(games: list) -> int:
    home_point = 0
    for score in games:
        if score[0] > score[-1]:
            home_point += 3
        elif score[0] == score[-1]:
            home_point += 1

    return home_point


def negative(number: int):
    s = "-" + str(number)
    return int(s)


def basic_op(operator: chr, value1: int, value2: int):
    if operator == '-':
        return value1 - value2
    if operator == '+':
        return value1 + value2
    if operator == '/':
        return value1 // value2
    else:
        return value1 * value2


def abbrev_name(name: str):
    import string
    initial = ''
    second_initial = ''
    for a in name:
        if a not in string.ascii_lowercase:
            if len(initial) == 0:
                initial = a
            else:
                second_initial = a
    return initial + '.' + second_initial


print(abbrev_name("Sam Harris"))
