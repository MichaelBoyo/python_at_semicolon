import random


def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1, die2


def display_dice(dice):
    die1, die2 = dice
    print(f"player rolled {die1} + {die2} = {sum(dice)}")


die_values = roll_dice()
display_dice(die_values)
sum_of_dice = sum(die_values)
