import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

islands = deque()
visited = [[False] * n for i in range(n)]


directions = [(1,0),(-1,0),(0,1),(0,-1)]
def BFS(graph, visited, i,j,idx,islands):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    islands.append((i,j))
    graph[i][j] = (idx,0)
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            sx,sy = x+dx, y+dy
            if 0<=sx<n and 0<=sy<n and not visited[sx][sy] and graph[sx][sy]==1:
                visited[sx][sy]=True
                queue.append((sx,sy))
                graph[sx][sy] = (idx,0)
                islands.append((sx,sy))


idx = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            BFS(graph,visited,i,j,idx,islands)
            idx+=1

dist = float("inf")
while True:
    new_islands = deque()
    while islands:
        x,y = islands.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<n:
                if graph[sx][sy] == 0:
                    new_islands.append((sx,sy))
                    graph[sx][sy] = (graph[x][y][0], graph[x][y][1]+1)
                
                elif not graph[sx][sy] == 0 and not graph[x][y][0] == graph[sx][sy][0]:
                    dist = min(dist, graph[sx][sy][1] + graph[x][y][1])
        
    if not dist == float("inf"):
        print(dist)
        exit()
    islands = new_islands