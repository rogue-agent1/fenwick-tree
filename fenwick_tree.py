#!/usr/bin/env python3
"""fenwick_tree - Binary indexed tree (Fenwick tree) for prefix sums."""
import sys

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    @classmethod
    def from_array(cls, data):
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
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    
    def range_sum(self, l, r):
        if l == 0:
            return self.prefix_sum(r)
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
    
    def find_kth(self, k):
        """Find smallest index with prefix sum >= k."""
        pos = 0
        bit_mask = 1
        while bit_mask <= self.n:
            bit_mask <<= 1
        bit_mask >>= 1
        while bit_mask > 0:
            next_pos = pos + bit_mask
            if next_pos <= self.n and self.tree[next_pos] < k:
                k -= self.tree[next_pos]
                pos = next_pos
            bit_mask >>= 1
        return pos

class FenwickTree2D:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tree = [[0]*(cols+1) for _ in range(rows+1)]
    
    def update(self, r, c, delta):
        r += 1
        while r <= self.rows:
            j = c + 1
            while j <= self.cols:
                self.tree[r][j] += delta
                j += j & (-j)
            r += r & (-r)
    
    def prefix_sum(self, r, c):
        s = 0
        r += 1
        while r > 0:
            j = c + 1
            while j > 0:
                s += self.tree[r][j]
                j -= j & (-j)
            r -= r & (-r)
        return s
    
    def range_sum(self, r1, c1, r2, c2):
        s = self.prefix_sum(r2, c2)
        if r1 > 0: s -= self.prefix_sum(r1-1, c2)
        if c1 > 0: s -= self.prefix_sum(r2, c1-1)
        if r1 > 0 and c1 > 0: s += self.prefix_sum(r1-1, c1-1)
        return s

def test():
    ft = FenwickTree.from_array([1, 2, 3, 4, 5])
    assert ft.prefix_sum(0) == 1
    assert ft.prefix_sum(2) == 6
    assert ft.prefix_sum(4) == 15
    assert ft.range_sum(1, 3) == 9
    
    ft.update(2, 5)  # 3 -> 8
    assert ft.prefix_sum(4) == 20
    assert ft.range_sum(2, 2) == 8
    
    # Find kth
    ft2 = FenwickTree.from_array([1, 0, 1, 0, 1])
    assert ft2.find_kth(1) == 0
    assert ft2.find_kth(2) == 2
    
    # 2D
    ft2d = FenwickTree2D(3, 3)
    ft2d.update(0, 0, 1)
    ft2d.update(1, 1, 2)
    ft2d.update(2, 2, 3)
    assert ft2d.prefix_sum(2, 2) == 6
    assert ft2d.range_sum(1, 1, 2, 2) == 5
    
    print("All tests passed!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: fenwick_tree.py test")
