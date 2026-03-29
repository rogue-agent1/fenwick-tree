#!/usr/bin/env python3
"""fenwick_tree - Binary Indexed Tree (Fenwick tree) for prefix sums."""
import sys

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)
    @classmethod
    def from_list(cls, arr):
        ft = cls(len(arr))
        for i, v in enumerate(arr):
            ft.update(i + 1, v)
        return ft

def test():
    ft = FenwickTree.from_list([1, 3, 5, 7, 9, 11])
    assert ft.query(3) == 9  # 1+3+5
    assert ft.query(6) == 36  # sum all
    assert ft.range_query(2, 5) == 24  # 3+5+7+9
    ft.update(3, 5)  # add 5 to position 3
    assert ft.query(3) == 14  # 1+3+10
    assert ft.range_query(3, 3) == 10
    print("OK: fenwick_tree")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: fenwick_tree.py test")
