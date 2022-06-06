import string

user_input = input("enter a word: ")
key = input("enter key: ")
while not user_input.isalpha():
    print("wrong word")
    user_input = input("enter a word: ")
while not key.isdigit() or not  1 < int(key) <= 26:
    print("wrong key.. enter key between 1 and 26")
    key = input("enter key: ")
if user_input.isalpha() and key.isdigit():
    key = int(key)
    abc = string.ascii_lowercase
    trans_abc = abc[key:] + abc[:key]
    encoded_word = user_input.translate(str.maketrans(abc, trans_abc))
    print("decoded word is" + encoded_word)

    a = int(input("enter 1 to decode: "))
    if a == 1:
        decoded_word = encoded_word.translate(str.maketrans(trans_abc, abc))
        print(decoded_word)
    else:
        print("gracias")
