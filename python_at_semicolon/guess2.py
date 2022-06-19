if __name__ == '__main__':
    import random

    random_number = (random.randint(0, 100))

    i = 0
    while i < 5:
        guess = int(input('guess number between 0-100: '))
        if guess < 0 or guess > 100:
            print("ori e ti yi mumu")
            break
        if random_number == guess:
            print('good guess.. bravo')
            break
        elif guess < random_number:
            print('too low')
        else:
            print("too high")
        i += 1
    else:
        print("you can never make it")
        print("the corrent number is", random_number)