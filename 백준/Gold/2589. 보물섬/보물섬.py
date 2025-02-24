import sys
from collections import deque

def DFS(graph,i,j,result):
    visited = [[False]*m for i in range(n)]
    visited[i][j] = True
    queue = deque()
    queue.append((i,j,0))
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        x,y,cnt = queue.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<len(graph) and 0<=sy <len(graph[0]) and not visited[sx][sy] and graph[sx][sy] == "L":
                visited[sx][sy] = True
                queue.append((sx,sy,cnt+1))

    result.append(cnt)         
    
n,m= map(int,sys.stdin.readline().split())

graph = [[] for i in range(n)]
for i in range(n):
    words = sys.stdin.readline().strip()
    for word in words:
        graph[i].append(word)


result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            DFS(graph,i,j,result)

print(max(result))