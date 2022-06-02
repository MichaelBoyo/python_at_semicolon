import random
random_number = (random.randint(0, 100))
guess = int(input('guess number: '))
while random_number != guess:
    if guess > random_number:
        print('too high')
    else:
        print('too low')
    guess = int(input('guess number: '))
if random_number == guess:
    print('good guess.. bravo')