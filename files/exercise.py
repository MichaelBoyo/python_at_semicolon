import csv
from pathlib import Path

numbers = [
    [1,3,4,5,6],
    [3,5,6,7,8,8],
    [3,4,5,6,7]
]
file_path = Path.home() /"numbers.csv"
with file_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    for row in numbers:
        writer.writerow(row)

file = file_path.open(mode="r", encoding="utf-8")
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()