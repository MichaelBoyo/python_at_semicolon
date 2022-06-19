import string


def encrypt(word: str, key: str) -> str:
    """
    this function encrypts a word
    :param word: str
    :param key: str
    :return: str
    """
    while not word.isalpha():
        print("wrong word")
        word = input("enter a word: ")
    while not key.isdigit() or not 1 < int(key) <= 26:
        print("wrong key.. enter key between 1 and 26")
        key = input("enter key: ")
    if word.isalpha() and key.isdigit():
        key = int(key)
        abc = string.ascii_lowercase
        trans_abc = abc[key:] + abc[:key]
        encoded_word = word.lower().translate(str.maketrans(abc, trans_abc))
        return encoded_word


def decrypt(encoded_word: str, key: str) -> str:
    """
       this function decrypts a word
       :param encoded_word: str
       :param key: str
       :return: str
       """
    key = int(key)
    abc = string.ascii_lowercase
    trans_abc = abc[key:] + abc[:key]
    return encoded_word.lower().translate(str.maketrans(trans_abc, abc))


# user_input = input("enter a word: ")
# user_key = input("enter key: ")
#
# encode = encrypt(user_input, user_key)
# print("encoded word is " + encode)
# de = decrypt(encode, user_key)