count = 1
a = 0
b =0
c = 0
d = 0
while count <= 5:
    name = input("enter your name: ")
    grade = input("enter letter grade: ")

    match grade:
        case "A":
            a += 1
        case "B":
            b += 1
        case "C":
            c += 1
        case "D":
            d += 1
    count += 1
print("A --> {}\n"
      "B --> {}\n"
      "C --> {}\n"
      "D --> {}\n".format(a, b, c, d))
