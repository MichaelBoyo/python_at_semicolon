def kata(lst: list, number: int) -> list:
    indexes = []
    for num in range(len(lst) - 1):
        for i in range(1, len(lst)):
            if lst[num] + lst[i] == number:
                indexes.append(num)
                indexes.append(i)
    return list(set(indexes))


def kata2(lst: list, number: int) -> list:
    return list(set([lst.index(a) for a in lst for b in lst[1:] if a + b == number]))


def kata3(lst, number):
    for j in range(len(lst) - 1):
        for i in range(1, len(lst)):
            if lst[j] + lst[i] == number:
                return [j, i]


def kata4(lst: list, number: int) -> list | int:
    map_ = {}
    for i in range(len(lst)):
        c = number - lst[i]
        if c in map_:
            return [map_[c], i]
        else:
            map_[lst[i]] = i
    return -1

#
# print(kata([3, 1, -8, 5], 6))
# print(kata2([3, 1, -8, 5], 6))
print(kata4([3, 1, -8, 5], 6))
