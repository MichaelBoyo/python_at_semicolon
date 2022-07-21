def grading_students(grades):
    lst = []
    n = grades[0]
    for a in grades[1:]:
        b = str(a)
        if b[-1] in "1234":
            num = a - int(b[-1])
            num += 5
            if num - a <= n and num > 40:
                lst.append(num)
            else:
                lst.append(a)
        else:
            num2 = a + int(b[-1])
            nn = str(num2)
            num2 -= int(nn[-1])
            if num2 - a <= n and num2 > 40:
                lst.append(num2)
            else:
                lst.append(a)
    return lst


print(grading_students([4, 73, 67, 38, 33]))
