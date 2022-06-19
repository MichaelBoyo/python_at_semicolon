word = "missile"
for x in word:
    if x == "z":
        print(x)
        break
else:
    print("-1")

for i in range(1, len(word)):
    if word[i] == "i":
        print(word[i])
        break
else:
    print("-1")

for index, letter in enumerate(word):
    if letter == "i":
        print(index, letter)
        break
else:
    print("-1")

print(f"{45:*>10d}")
print(f"{45:*<+10d}")
print(f"{-11:*^10d}")