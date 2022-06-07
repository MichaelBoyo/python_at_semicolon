number_of_input = int(input("how many values do you want to enter? "))
i = 1
num = []
while i <= number_of_input:
    number = int(input("enter numbers: "))
    num.append(number)
    i += 1
print(num)
max_no = max(num)
min_no = min(num)
print("sum of extremes {} and {} is {}".format(max_no, min_no, max_no + min_no))