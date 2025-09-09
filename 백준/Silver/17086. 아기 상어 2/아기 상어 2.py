import sys
from collections import deque

input = sys.stdin.readline

dirs = [-1,0,1]

n,m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


def BFS(i,j):
    visited = [[False] * m for i in range(n)]
    visited[i][j] = True
    queue = deque()
    queue.append((i,j,0))
    while queue:
        x,y,cnt = queue.popleft()
        for dx in dirs:
            for dy in dirs:
                sx,sy = x+dx, y+dy
                if 0<=sx<n and 0<=sy<m and not visited[sx][sy]:
                    if graph[sx][sy] == 1:
                        return cnt+1
                    elif graph[sx][sy] == 0:
                        queue.append((sx,sy,cnt+1))
                        visited[sx][sy] = True
    return cnt

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer = max(BFS(i,j),answer)

print(answer)