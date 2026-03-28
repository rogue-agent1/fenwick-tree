#!/usr/bin/env python3
"""fenwick_tree - Binary indexed tree (Fenwick tree)."""
import sys
class Fenwick:
    def __init__(s,n):s.n=n;s.tree=[0]*(n+1)
    @classmethod
    def from_array(cls,arr):
        f=cls(len(arr))
        for i,v in enumerate(arr):f.update(i,v)
        return f
    def update(s,i,delta):
        i+=1
        while i<=s.n:s.tree[i]+=delta;i+=i&(-i)
    def prefix_sum(s,i):
        i+=1;total=0
        while i>0:total+=s.tree[i];i-=i&(-i)
        return total
    def range_sum(s,l,r):return s.prefix_sum(r)-(s.prefix_sum(l-1) if l>0 else 0)
    def find_kth(s,k):
        pos=0;bitmask=1
        while bitmask<=s.n:bitmask<<=1
        bitmask>>=1
        while bitmask:
            nxt=pos+bitmask
            if nxt<=s.n and s.tree[nxt]<k:k-=s.tree[nxt];pos=nxt
            bitmask>>=1
        return pos
if __name__=="__main__":
    data=[3,2,4,5,1,1,5,3];f=Fenwick.from_array(data);print(f"Data: {data}")
    print(f"Prefix sum [0..4]: {f.prefix_sum(4)}");print(f"Range sum [2..5]: {f.range_sum(2,5)}")
    f.update(3,6);print(f"After +6 at index 3:");print(f"Prefix sum [0..4]: {f.prefix_sum(4)}")
