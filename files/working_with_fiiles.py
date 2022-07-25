from pathlib import Path

# path = Path(r"C:/Users/Michael/PycharmProjects/pythonAtSemi/code_wars/apples.py")
# with path.open(mode="r", encoding="utf-8") as file:
#     text = file.read()
#
# with path.open(mode="r", encoding="utf-8") as file:
#     for line in file.readlines():
#         print(line, end=" ")
texts = """the lord i smy shepherd 
i shall not want
"""

# path = Path(r"C:/Users/Michael/hello.txt")
# with path.open(mode="w", encoding="utf-8") as file:
#     file.write(texts)
temps = [55, 77, 88, 99, 90, 00, 67]
file_path = Path.home() / "temperature.txt"
with file_path.open(mode="w", encoding="utf-8") as file:
    file.write(str(temps[0]))
    for temp in temps[1:]:
        file.write(f",{temp}")

with file_path.open(mode="r", encoding="utf-8") as file:
    text = file.read()


print([int(a) for a in text.split(",")])