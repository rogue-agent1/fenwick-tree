import argparse

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

def main():
    p = argparse.ArgumentParser(description="Fenwick tree")
    p.add_argument("--demo", action="store_true")
    p.add_argument("--values", nargs="+", type=int)
    p.add_argument("--query", nargs=2, type=int, metavar=("L", "R"))
    args = p.parse_args()
    if args.demo:
        vals = [1, 3, 5, 7, 9, 11]
        ft = FenwickTree(len(vals))
        for i, v in enumerate(vals): ft.update(i, v)
        print(f"Values: {vals}")
        print(f"Prefix sum [0..2]: {ft.prefix_sum(2)}")
        print(f"Range sum [1..4]:  {ft.range_sum(1, 4)}")
        ft.update(2, 3)
        print(f"After +3 at index 2:")
        print(f"Prefix sum [0..2]: {ft.prefix_sum(2)}")
    elif args.values:
        ft = FenwickTree(len(args.values))
        for i, v in enumerate(args.values): ft.update(i, v)
        if args.query: print(ft.range_sum(args.query[0], args.query[1]))
        else:
            for i in range(len(args.values)):
                print(f"prefix[{i}] = {ft.prefix_sum(i)}")
    else: p.print_help()

if __name__ == "__main__":
    main()
