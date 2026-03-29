#!/usr/bin/env python3
"""Fenwick tree (Binary Indexed Tree). Zero dependencies."""

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    @classmethod
    def from_list(cls, data):
        ft = cls(len(data))
        for i, v in enumerate(data):
            ft.update(i, v)
        return ft

    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def prefix_sum(self, i):
        s = 0; i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def range_sum(self, l, r):
        if l == 0: return self.prefix_sum(r)
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

    def point_query(self, i):
        return self.range_sum(i, i)

    def find_kth(self, k):
        """Find smallest index with prefix sum >= k."""
        pos = 0; bit = 1
        while bit <= self.n: bit <<= 1
        bit >>= 1
        while bit > 0:
            nxt = pos + bit
            if nxt <= self.n and self.tree[nxt] < k:
                k -= self.tree[nxt]
                pos = nxt
            bit >>= 1
        return pos

if __name__ == "__main__":
    ft = FenwickTree.from_list([1, 2, 3, 4, 5])
    print(f"Sum [0,4] = {ft.prefix_sum(4)}")
    print(f"Sum [1,3] = {ft.range_sum(1,3)}")
