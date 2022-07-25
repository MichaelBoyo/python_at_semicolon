def is_pangram(s: str):
    import string
    abc, count, lower = string.ascii_lowercase, 0, s.lower()
    for a in abc:
        if a in lower:
            count += 1
    if count == len(abc):
        return True
    return False


def largest_str(lst: list, stop: int):
    lev = []
    s = ""
    start = 0
    for b in range(len(lst)):
        for i in range(start, stop):
            s += lst[i]
        lev.append(s)
        s = ''
        if stop <= len(lst) - 1:
            start += 1
            stop += 1
    lev.sort(key=len, reverse=True)
    return lev[0]


print(largest_str(['koko', 'panda', 'kiki', 'ola', 'onigurete'], 2))



# print(is_pangram("The quick brown fox jumps over the lazy dog"))
