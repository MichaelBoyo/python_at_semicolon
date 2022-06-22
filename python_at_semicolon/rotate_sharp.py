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
            if (b == ")" and peaked == "(") or\
                    (b == "}" and peaked == "{") or \
                    (b == "]" and peaked == "["):
                stack.pop()
            else:
                return False
        else:
            return False

    return True


print(bracket_pair("{}{[()]}"))
