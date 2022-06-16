import math


def get_digit(number, index):
    return number // (10 ** index) % 10


print(get_digit(2374, 3))


def get_vertex():
    x = float(input("enter x:"))
    y = float(input("enter y:"))
    return x, y


def get_triangle():
    print("first vertex")
    x1, y1 = get_vertex()
    print("second vertex")
    x2, y2 = get_vertex()
    print("third vertex")
    x3, y3 = get_vertex()


# def side_length(x1,y1,x2,y2):
#     return math.sqrt((x1,y1))
# def calculate_area():
#     a = side_length(x1,y1,x2,y2)
