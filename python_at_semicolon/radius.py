import math

radius_int = int(input("Enter the radius of your cirle:"))
circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int **2)

print("The circumference is:",round(circumference,2),",and the area is:",round(area,2))