import csv
from pathlib import Path

daily_temperatures = [
    [56, 77, 88, 78, 99, 77],
    [78, 99, 88, 67, 89, 77],
    [67, 89, 99, 87, 99, 75],
]
file_path = Path.home() / "temperatures.csv"
with file_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(daily_temperatures)

file_ = file_path.open(mode="r", encoding="utf-8")
reader = csv.reader(file_)
for row in reader:
    print(row)
file.close()
