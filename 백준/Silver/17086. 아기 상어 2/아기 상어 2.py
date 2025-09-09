import sys
from collections import deque

input = sys.stdin.readline

dirs = [-1,0,1]

n,m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

def BFS(queue, visited):
    while queue:
        x,y = queue.popleft()
        for dx in dirs:
            for dy in dirs:
                sx,sy = x+dx, y+dy
                if 0<=sx<n and 0<=sy<m and visited[sx][sy] == -1:
                    visited[sx][sy] = visited[x][y] +1
                    queue.append((sx,sy))

answer = 0
queue = deque()
visited = [[-1] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 0

BFS(queue,visited)
for i in range(n):
    for j in range(m):
        answer = max(answer, visited[i][j])

print(answer)