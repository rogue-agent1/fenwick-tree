from fenwick_tree import FenwickTree
ft = FenwickTree.from_list([1, 2, 3, 4, 5])
assert ft.prefix_sum(4) == 15
assert ft.prefix_sum(0) == 1
assert ft.range_sum(1, 3) == 9
assert ft.point_query(2) == 3
ft.update(2, 7)  # add 7 to index 2
assert ft.point_query(2) == 10
assert ft.prefix_sum(4) == 22
# find_kth
ft2 = FenwickTree.from_list([1, 0, 1, 0, 1])
assert ft2.find_kth(1) == 0
assert ft2.find_kth(2) == 2
print("fenwick_tree tests passed")
