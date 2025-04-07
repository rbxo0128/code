import sys
from collections import deque

n,m= map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))
    
max_cnt = 0
check = set()
directions = [(1,0),(-1,0),(0,1),(0,-1)]

def DFS(x,y,cnt):
    global max_cnt
    check.add(graph[x][y])
    max_cnt = max(max_cnt,cnt)
    for dx,dy in directions:
        sx,sy = x+dx,y+dy

        if 0<=sx<n and 0<=sy<m and not graph[sx][sy] in check:
            DFS(sx,sy,cnt+1)

    check.remove(graph[x][y])

DFS(0,0,1)
print(max_cnt)