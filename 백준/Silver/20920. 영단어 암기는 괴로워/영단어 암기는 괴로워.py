import sys
from collections import defaultdict

input = sys.stdin.readline

n,m = map(int,input().split())
arr = defaultdict(int)

for i in range(n):
    word = input().strip()
    if len(word) < m:
        continue

    arr[word] += 1

for word in sorted(arr, key= lambda x:(-arr[x],-len(x),x)):
    print(word)