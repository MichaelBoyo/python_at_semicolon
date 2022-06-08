sentinel = 0
while sentinel != -1:
    eggs = int(input("enter no of eggs or 0 to end: "))
    if eggs == 0:
        sentinel = -1
    else:
        no_of_boxes = eggs // 6
        remaining = no_of_boxes % 28
        if not eggs % 6:
            print("you needs {} boxes to store {} eggs".format(no_of_boxes, eggs))
        else:
            print("you needs {} boxes to store {} eggs".format(no_of_boxes+1, eggs))
            print("{} eggs are in the last box and {} additional eggs are needed to fill it".format(remaining, 6 - remaining))