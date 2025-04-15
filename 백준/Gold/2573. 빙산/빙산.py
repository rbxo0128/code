import sys
from collections import deque

def BFS(graph,near):
    global n,m
    directions = [(-1,0),(0,-1),(0,1),(1,0)]
    new_near = deque()
    while near:
        x,y = near.popleft()
        isnear = False
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<= sx < n and 0<= sy < m:
                if graph[sx][sy] != 0:
                    graph[sx][sy] -= 1
                    isnear = True
                    if graph[sx][sy] == 0:
                        new_near.append([sx,sy])
        if isnear:
            new_near.append([x,y])

    return new_near
                        
def BFS2(graph, visited, i,j):
    global n,m
    directions = [(-1,0),(0,-1),(0,1),(1,0)]
    visited[i][j] = True
    stack = deque()
    stack.append((i,j))
    while stack:
        x,y = stack.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<= sx<n and 0<=sy<m and not visited[sx][sy]:
                if graph[sx][sy] != 0:
                    visited[sx][sy] = True
                    stack.append((sx,sy))
    
n,m = map(int,sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


near = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            near.append([i,j])

day = 0

while True:
    near =  BFS(graph,near)
    if sum(sum(i) for i in graph) == 0:
        print(0)
        break
    
    visited = [[False] * m for i in range(n)]
    cnt = 0
    day += 1
    stop = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                cnt += 1
                if cnt == 2:
                    stop = True
                    print(day)
                    break
                BFS2(graph,visited,i,j)
        if stop:
            break
    if stop:
        break
