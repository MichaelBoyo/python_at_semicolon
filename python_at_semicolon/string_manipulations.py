s = "hello world"
print(s.find("o", 1, 3))
print(s.index("l"))
print(s.isalpha())
print(s.isdigit())
print(s.capitalize())
print(s.startswith("h"))
print(s.endswith("o"))
print(s.split())
print(s.removeprefix("hello "))
print(s.swapcase())

tct = "34"
print(tct.zfill(5))
print(ord("r"))
print("l" in s)
print(s.replace("lo", "er", 1))
i = "10110110"
g = (i.replace("1", "2").replace("0", "1").replace("2", "0"))
print(g)
print(i.translate(str.maketrans("01", "10")))
