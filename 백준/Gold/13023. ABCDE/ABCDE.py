import sys
import math
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

dict = {i : [] for i in range(n)}

for i in range(m):
    x,y = map(int,input().split())
    dict[x].append(y)
    dict[y].append(x)

def DFS(level, visited, idx):
    if level == 5:
        print(1)
        exit()

    if idx == None:
        for i in range(n):
            DFS(level+1, visited | {i}, i)

    else:
        for i in dict[idx]:
            if i not in visited:
                DFS(level+1, visited | {i}, i)

DFS(0,set(), None)
print(0)