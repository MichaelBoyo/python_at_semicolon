def anagram(number):
    square = str(int(number) * int(number))
    print(f"the square of %s is %s" % (number, square))
    if len(number) == 1:
        if square[len(square) - 1] == number:
            print("the number is an anagram")
    elif len(number) > 1:
        new_num = square[len(square) - 1] + square[len(square) - 2]
        print(f"the last %d numbers is %s " % (len(number), new_num))
        print(f"%s is not equal to %s " % (number, new_num))
        if number == new_num:
            print("therefore, number is an anagram")
        else:
            print("therefore, the number is not an anagram")


user_input = input("enter a number: ")
anagram(user_input)
