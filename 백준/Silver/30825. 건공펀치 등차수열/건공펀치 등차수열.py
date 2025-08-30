import sys

n,m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

base = -float("inf")
idx = -1
for i in range(n):
    if arr[i] - m*i > base:
        base = arr[i] - m * i
        idx = i

print(m*(n)*(n-1)//2+(arr[idx]-m*idx)*n-sum(arr))