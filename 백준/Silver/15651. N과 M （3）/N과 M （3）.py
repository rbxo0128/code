import sys
from itertools import product

input = sys.stdin.readline

n,m = map(int,input().split())

arr = [i for i in range(1,n+1)]
for i in product(arr, repeat=m):
    print(' '.join(map(str, i)))
