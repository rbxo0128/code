import sys
from collections import deque

def BFS(graph, n, m ,h):
    visited = [[[False]*m for _ in range(n)] for _ in range(h)]
    stack = deque()
    directions = [(0,0,1),(0,0,-1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]
    cnt = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if graph[k][i][j] == 1:
                    stack.append((i,j,k,0))
    
    while stack:
        x,y,z,cnt = stack.popleft()
        for dx,dy,dz in directions:
            sx,sy,sz = x+dx,y+dy,z+dz
            if 0<=sx<n and 0<=sy<m and 0<=sz<h and not visited[sz][sx][sy]:
                if graph[sz][sx][sy] == 0:
                    visited[sz][sx][sy] = True
                    graph[sz][sx][sy] = 1
                    stack.append((sx,sy,sz,cnt+1))
                    
    return cnt
    
                


m,n,h = map(int, sys.stdin.readline().split())

graph = [[] for i in range(h)]
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, sys.stdin.readline().split())))

day = BFS(graph, n,m,h)

count = 0
tomato = False
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                count+=1
                tomato = True
                break
        if tomato:
            break
    if tomato:
        break

if count == 0:
    print(day)
else:
    print(-1)
