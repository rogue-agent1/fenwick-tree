#!/usr/bin/env python3
"""fenwick_tree - BIT for prefix sums, range updates, order stats."""
import sys, argparse, json

class FenwickTree:
    def __init__(self, n):
        self.n = n; self.tree = [0] * (n + 1)
    def update(self, i, delta):
        i += 1
        while i <= self.n: self.tree[i] += delta; i += i & (-i)
    def prefix_sum(self, i):
        i += 1; s = 0
        while i > 0: s += self.tree[i]; i -= i & (-i)
        return s
    def range_sum(self, l, r):
        return self.prefix_sum(r) - (self.prefix_sum(l-1) if l > 0 else 0)
    def find_kth(self, k):
        """Find smallest index with prefix sum >= k."""
        pos = 0; bit_mask = 1
        while bit_mask <= self.n: bit_mask <<= 1
        bit_mask >>= 1
        while bit_mask > 0:
            next_pos = pos + bit_mask
            if next_pos <= self.n and self.tree[next_pos] < k:
                k -= self.tree[next_pos]; pos = next_pos
            bit_mask >>= 1
        return pos

class FenwickRange:
    """Supports range updates and range queries."""
    def __init__(self, n):
        self.n = n; self.b1 = FenwickTree(n); self.b2 = FenwickTree(n)
    def _add(self, b, i, delta):
        i += 1
        while i <= self.n: b.tree[i] += delta; i += i & (-i)
    def range_add(self, l, r, val):
        self._add(self.b1, l, val); self._add(self.b1, r+1, -val)
        self._add(self.b2, l, val*(l-1)); self._add(self.b2, r+1, -val*r)
    def prefix_sum(self, i):
        return self.b1.prefix_sum(i) * i - self.b2.prefix_sum(i)
    def range_sum(self, l, r):
        return self.prefix_sum(r) - (self.prefix_sum(l-1) if l > 0 else 0)

def main():
    p = argparse.ArgumentParser(description="Fenwick tree")
    p.add_argument("--demo", action="store_true")
    args = p.parse_args()
    if args.demo:
        print("=== Point Update, Range Query ===")
        ft = FenwickTree(10)
        for i in range(10): ft.update(i, i+1)
        print(f"Prefix sum [0..4]: {ft.prefix_sum(4)}")
        print(f"Range sum [3..7]: {ft.range_sum(3, 7)}")
        ft.update(3, 10)
        print(f"After +10 at idx 3, range [3..7]: {ft.range_sum(3, 7)}")
        print(f"\n=== Order Statistics ===")
        ost = FenwickTree(100)
        for v in [5, 10, 15, 20, 25, 30]: ost.update(v, 1)
        print(f"3rd smallest: {ost.find_kth(3)}")
        print(f"\n=== Range Update, Range Query ===")
        fr = FenwickRange(10)
        fr.range_add(2, 5, 3)
        fr.range_add(4, 8, 2)
        print(f"Range sum [0..9]: {fr.range_sum(0, 9)}")
        print(f"Range sum [3..6]: {fr.range_sum(3, 6)}")
    else: p.print_help()
if __name__ == "__main__": main()
