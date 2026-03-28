#!/usr/bin/env python3
"""Fenwick tree (Binary Indexed Tree) for prefix sums."""
import sys
class FenwickTree:
    def __init__(self,n):
        self.n=n;self.tree=[0]*(n+1)
    def update(self,i,delta):
        while i<=self.n: self.tree[i]+=delta; i+=i&(-i)
    def query(self,i):
        s=0
        while i>0: s+=self.tree[i]; i-=i&(-i)
        return s
    def range_query(self,l,r): return self.query(r)-self.query(l-1)
    @classmethod
    def from_array(cls,arr):
        ft=cls(len(arr))
        for i,v in enumerate(arr): ft.update(i+1,v)
        return ft
def main():
    arr=[3,2,5,1,7,4,8,6]
    ft=FenwickTree.from_array(arr)
    print(f"Array: {arr}")
    print(f"Prefix sum [1..4]: {ft.query(4)}")
    print(f"Range sum [3..6]: {ft.range_query(3,6)}")
    ft.update(3,10)  # arr[2]+=10
    print(f"After arr[2]+=10, prefix sum [1..4]: {ft.query(4)}")
if __name__=="__main__": main()
