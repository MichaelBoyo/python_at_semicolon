import math
print("{:<4s}{:>24}".format("Hour", "Number of Bacteria"))

for x in range(0, 16, 5):
    print("{:>4d}{:>24}".format(x, 200*int(math.pow(2, x))))