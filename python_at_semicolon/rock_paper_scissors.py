import random
count = 1
player_score = 0
comp_score = 0
pr = "player chose"
while count <= 5:
    user_in = input("R --> Rock\n"
                    "P --> Paper\n"
                    "S --> Scissors\n")
    game = ["R", "P", "S"]
    match user_in:
        case "R":
            print("{} rock".format(pr))
        case "P":
            print("{} paper".format(pr))
        case "S":
            print("{} scissors".format(pr))
    rand_num = random.randint(0, 2)
    comp = game[rand_num]
    co = "Computer chose"
    match comp:
        case "R":
            print("{} rock".format(co))
        case "P":
            print("{} paper".format(co))
        case "S":
            print("{} scissors".format(co))

    if comp == "R" and user_in == "S" or comp == "S" and user_in == "P" or comp == "P" and user_in == "R":
        print("comp wins")
        comp_score += 1
    elif comp == "R" and user_in == "R" or comp == "S" and user_in == "S" or comp == "P" and user_in == "P":
        print("DRAW")
    else:
        print("player wins")
        player_score += 1
    count += 1
print("player won {} times".format(player_score))
print("comp won {} times".format(comp_score))