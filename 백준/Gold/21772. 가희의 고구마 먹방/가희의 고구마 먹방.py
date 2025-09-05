import sys
from collections import deque

n,m, T = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == "G":
            graph[i][j] = "."
            x,y = i,j

directions = [(0,1),(0,-1),(1,0),(-1,0)]
results = []
def DFS(x,y,moves,cnt):
    if moves == T:
        results.append(cnt)
        return
    
    can_move = False
    for dx,dy in directions:
        sx,sy = x+dx,y+dy

        if 0<=sx<n and 0<=sy<m:
            if graph[sx][sy] == "S":
                graph[sx][sy] = "."
                can_move = True
                DFS(sx,sy,moves+1,cnt+1)
                graph[sx][sy] = "S"
            elif graph[sx][sy] == ".":
                can_move = True
                DFS(sx,sy,moves+1,cnt)

    if not can_move:
        results.append(cnt)

DFS(x,y,0,0)
if not results:
    print(0)
else:
    print(max(results))