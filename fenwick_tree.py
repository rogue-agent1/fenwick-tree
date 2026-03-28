#!/usr/bin/env python3
"""Fenwick Tree (Binary Indexed Tree) — zero-dep."""

class FenwickTree:
    def __init__(self, n):
        self.n=n; self.tree=[0]*(n+1)
    def update(self, i, delta):
        while i<=self.n: self.tree[i]+=delta; i+=i&(-i)
    def query(self, i):
        s=0
        while i>0: s+=self.tree[i]; i-=i&(-i)
        return s
    def range_query(self, l, r):
        return self.query(r)-(self.query(l-1) if l>1 else 0)
    @classmethod
    def from_array(cls, arr):
        ft=cls(len(arr))
        for i,v in enumerate(arr): ft.update(i+1,v)
        return ft

class FenwickTree2D:
    def __init__(self, rows, cols):
        self.rows=rows; self.cols=cols
        self.tree=[[0]*(cols+1) for _ in range(rows+1)]
    def update(self, r, c, delta):
        i=r
        while i<=self.rows:
            j=c
            while j<=self.cols: self.tree[i][j]+=delta; j+=j&(-j)
            i+=i&(-i)
    def query(self, r, c):
        s=0; i=r
        while i>0:
            j=c
            while j>0: s+=self.tree[i][j]; j-=j&(-j)
            i-=i&(-i)
        return s

if __name__=="__main__":
    arr=[3,2,5,1,4,6,2,8]
    ft=FenwickTree.from_array(arr)
    print(f"Array: {arr}")
    print(f"Prefix sum [1..5]: {ft.query(5)}")
    print(f"Range sum [2..6]: {ft.range_query(2,6)}")
    ft.update(3,10)  # arr[2] += 10
    print(f"After arr[2]+=10, prefix [1..5]: {ft.query(5)}")
    # 2D
    ft2=FenwickTree2D(3,3)
    ft2.update(1,1,5); ft2.update(2,2,3); ft2.update(1,2,1)
    print(f"\n2D query (1,1)-(2,2): {ft2.query(2,2)}")
