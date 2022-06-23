set_a = {1, 2, 3, 4, 5}
set_b = {4, 6, 7, 8, 9}

print(set_a.union(set_b))
set_b |= set_a  # union_update
print(set_b.intersection(set_a))
print(set_b.union(set_a))
set_b &= set_a  # intersection_update
set_b -= set_a  # difference_update
set_b ^= set_a  # symmetric_difference_update
print(set_b)

var = set_b < set_a  # subset
var2 = set_b > set_a  # superset

