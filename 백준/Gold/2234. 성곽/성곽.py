import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for i in range(n)]

directions = [(0,-1),(-1,0),(0,1),(1,0)]

def BFS(i,j,idx):
    queue = deque()
    queue.append((i,j))
    cnt = 1
    visited[i][j] = True
    new = [(i,j)]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            if not graph[x][y] & (1 << i):
                dx,dy = directions[i]
                sx,sy = x+dx,y+dy
                if 0<=sx<n and 0<=sy<m and not visited[sx][sy]:
                    queue.append((sx,sy))
                    new.append((sx,sy))
                    cnt += 1
                    visited[sx][sy] = True

    for x,y in new:
        graph[x][y] = (cnt,idx)
    
    return cnt

idx = 0
max_room = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            max_room = max(BFS(i,j,idx),max_room)
            idx += 1

two_room = 0
for i in range(n):
    for j in range(m):
        for dx,dy in directions:
            sx,sy = i+dx,j+dy
            if 0<=sx<n and 0<=sy<m and graph[i][j][1] != graph[sx][sy][1]:
                two_room = max(two_room, graph[sx][sy][0] + graph[i][j][0])
print(idx)
print(max_room)
print(two_room)