def rotate(lst: list[int], k: int) -> list[int]:
    k = k % len(lst)
    return lst[k:] + lst[:k]


# print(rotate([1, 5, 7, 8, 9, 9, 90, 98], 2))
# print(-8 % 5)


def bracket_pair(brackets: str) -> bool:
    if len(brackets) < 2 or len(brackets) % 2 != 0:
        return False
    stack = []
    for b in brackets:
        if b in "{[(":
            stack.append(b)
        elif b in ")]}":
            peaked = stack[-1]
            if (b == ")" and peaked == "(") or \
                    (b == "}" and peaked == "{") or \
                    (b == "]" and peaked == "["):
                stack.pop()
            else:
                return False
        else:
            return False

    return True


# print(bracket_pair("{}{[()]}"))


def histogram(word):
    import string
    abc = string.ascii_lowercase
    print(abc[0])
    map_ = {}

    for char in abc:
        map_[char] = word.lower().count(char)
    return map_


def histogram_2(word):
    import string
    return {char: word.lower().count(char) for char in string.ascii_lowercase}


def unique_values(word: str) -> int:
    count = 0
    for letter in word:
        if word.count(letter) > 1:
            count += 1
    return count


# print(histogram_2("no language is useless"))
histogram("")
# print(unique_values("america"))
