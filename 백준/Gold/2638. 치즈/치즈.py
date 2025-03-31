import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


def BFS():
    visited = [[False]*m for i in range(n)]
    visited2 = [[False]*m for i in range(n)]

    visited[0][0] = True
    stack = deque()
    stack.append((0,0))
    while stack:
        x,y = stack.popleft()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m and not visited[sx][sy]:
                if graph[sx][sy] == 0:
                    stack.append((sx,sy))
                    visited[sx][sy] = True
                
                elif graph[sx][sy] == 1:
                    if visited2[sx][sy]:
                        graph[sx][sy] = 0
                        visited[sx][sy] = True

                    visited2[sx][sy] = True
    

day = 0
while True:
    if sum(sum(i) for i in graph) == 0:
        break
    day+=1
    BFS()


print(day)