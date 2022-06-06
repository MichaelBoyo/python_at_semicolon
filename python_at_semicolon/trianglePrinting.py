for a in range(1, 11):
    print("*" * a)

for a in range(11, 0, -1):
    print("*" * a)

for a in range(1, 19, 2):
    print(f'{"*" * a:>19}', end="")
    print(f'{"*" * a:<19}')
