import sys
from collections import deque

def BFS(graph):
    global start
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    stack = deque()
    
    n= len(graph)
    m = len(graph[0])
    while start:
        x,y = start.popleft()
        for dx,dy in directions:
            sx, sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m:
                if graph[sx][sy] == "X":
                    stack.append((sx,sy))
                    graph[sx][sy] = "."

    start = stack

graph = []
n,m = map(int,sys.stdin.readline().split())

for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))


duck = []

start = deque()
day = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != "X":
            start.append((i,j))
        if graph[i][j] == "L":
            duck.append((i,j))

duckqueue = deque()
duckqueue.append(duck[0])
visited = [[False]*m for i in range(n)]
visited[duck[0][0]][duck[0][1]] = True
duckqueue2 = deque()

day = 0
found = False
directions = [(0,1), (0,-1), (1,0), (-1,0)]

while not found:
    while duckqueue:
        x, y = duckqueue.popleft()
        if (x, y) == duck[1]:
            found = True
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == '.':
                    duckqueue.append((nx, ny))
                else:
                    duckqueue2.append((nx, ny))
    if found:
        print(day-1)
        break

    BFS(graph)
    day += 1

    duckqueue = duckqueue2
    duckqueue2 = deque()

