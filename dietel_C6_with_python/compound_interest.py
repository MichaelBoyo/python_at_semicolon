import math
p = 1000
r = 0.05 + 1
while r < 1.1:
    print("{:10s}{:10s}".format("Year", "Amount"))

    for i in range(1, 11):
        a = p * pow(r, i)
        print("{:4d}{:13.2f}".format(i, a))
    print()
    r += 0.01