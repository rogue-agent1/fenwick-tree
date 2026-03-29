#!/usr/bin/env python3
"""fenwick_tree - Binary indexed tree for prefix sums."""
import sys, argparse, json

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
        return self.prefix_sum(r) - (self.prefix_sum(l-1) if l > 0 else 0)
    @classmethod
    def from_array(cls, arr):
        ft = cls(len(arr))
        for i, v in enumerate(arr):
            ft.update(i, v)
        return ft

def main():
    p = argparse.ArgumentParser(description="Fenwick tree CLI")
    p.add_argument("values", nargs="+", type=float)
    p.add_argument("--range", nargs=2, type=int, metavar=("L","R"))
    p.add_argument("--prefix", type=int)
    args = p.parse_args()
    ft = FenwickTree.from_array(args.values)
    result = {"size": ft.n}
    if args.range:
        result["range_sum"] = {"l": args.range[0], "r": args.range[1], "sum": ft.range_sum(args.range[0], args.range[1])}
    if args.prefix is not None:
        result["prefix_sum"] = {"index": args.prefix, "sum": ft.prefix_sum(args.prefix)}
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
