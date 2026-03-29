#!/usr/bin/env python3
"""Fenwick tree (Binary Indexed Tree) for prefix sums and updates."""
import sys

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    def prefix_sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    def range_sum(self, l, r):
        if l == 0: return self.prefix_sum(r)
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
    @classmethod
    def from_list(cls, arr):
        ft = cls(len(arr))
        for i, v in enumerate(arr):
            ft.update(i, v)
        return ft

def test():
    ft = FenwickTree.from_list([1, 3, 5, 7, 9, 11])
    assert ft.prefix_sum(0) == 1
    assert ft.prefix_sum(2) == 9
    assert ft.prefix_sum(5) == 36
    assert ft.range_sum(1, 3) == 15
    ft.update(2, 5)  # arr[2] += 5 → 10
    assert ft.prefix_sum(2) == 14
    assert ft.range_sum(2, 2) == 10
    print("  fenwick_tree: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("Fenwick Tree (BIT)")
