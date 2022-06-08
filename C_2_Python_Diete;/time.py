time = int(input("enter no of seconds greater than 3600"))
minutes = time // 60
hour = minutes // 60
seconds = time % 60
if minutes > 60:
    minutes = minutes - 60
print(f"{hour=:<4}{minutes=:<4}{seconds=:<4}")

