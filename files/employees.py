import csv
from pathlib import Path

people = [
    {"name": "veronica", "age": 37},
    {"name": "mike", "age": 67},
    {"name": "kiki", "age": 17}
]
file_path = Path.home() / "people.csv"
file = file_path.open(mode="w", encoding="utf-8")
writer = csv.DictWriter(file, fieldnames=["name", "age"])
writer.writeheader()
writer.writerows(people)
file.close()
