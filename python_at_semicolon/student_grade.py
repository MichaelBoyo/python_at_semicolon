if __name__ == '__main__':
    args = int(input("enter score: "))
    if 45 <= args < 50:
        print("D")
    elif 40 <= args < 45:
        print("E")
    elif 60 <= args < 70:
        print("B")
    elif 50 <= args < 60:
        print("C")
    elif 70 <= args < 100:
        print("A")
    else:
        print("F")    