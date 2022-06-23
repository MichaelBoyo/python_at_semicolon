d1 = {'a': 1, 'b': 2, 'c': 3}
d1.pop('a')  # remove item via key
d1.popitem()  # remove last item in dict
d1.clear()  # clears dict
d1.update({'a': 5, 'b': 8})  # update dict
d1 |= {'a': 5, 'b': 8}  # another update method
print(list(d1.items()))  # gets both item and keys
print(list(d1.keys()))  # gets only keys
print(list(d1.values()))  # gets only values
print(d1)

for key in d1:  # this loop ordinarily returns keys
    print(key)

for key in d1:  # gets the values themselves
    print(d1[key])

for values in d1.values():  # another way to get the values from a dict
    print(values)
