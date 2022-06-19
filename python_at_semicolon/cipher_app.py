import ceasar_cipher


def encode():
    word = input("enter word")
    key = input("enter key")
    encoded_word = ceasar_cipher.encrypt(word, key)
    print("encoded successfully, encoded word is " + encoded_word)


def decode():
    word = input("enter encoded word")
    key = input("enter key")
    decoded_word = ceasar_cipher.decrypt(word, key)
    print("decoded successfully, decoded word is " + decoded_word)


if __name__ == '__main__':
    sentinel = 0
    while sentinel != -1:
        user = int(input("""
        Enter 1 to encode a message
        Enter 2 to decode a message
        Enter 0 to end
        """))

        match user:
            case 1:
                encode()
            case 2:
                decode()
            case 0:
                sentinel = -1
