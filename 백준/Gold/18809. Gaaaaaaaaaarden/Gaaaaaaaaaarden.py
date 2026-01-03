import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def BFS(green,red):
    visited = [[[-1, -1] for i in range(m)] for i in range(n)]

    queue = deque()
    for x,y in green:
        visited[x][y] = [0,0]
        queue.append((x,y,0))
    for x,y in red:
        visited[x][y] = [0,1]
        queue.append((x,y,1))

    flowers = 0

    while queue:
        x,y,color = queue.popleft()
 
        if visited[x][y][1] == 3:
            continue
 
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m and graph[sx][sy] == 1:
                if visited[sx][sy][0] == -1:
                    visited[sx][sy] = [visited[x][y][0] + 1, color]
                    queue.append((sx, sy, color))

                elif visited[sx][sy][1] != color and visited[sx][sy][1] != 3:
                    if visited[sx][sy][0] == visited[x][y][0] + 1:
                        flowers += 1
                        visited[sx][sy][1] = 3

    return flowers

n,m,x,y = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

grounds = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            graph[i][j] = 1
            grounds.append((i,j))

max_flowers = 0
for green in combinations(grounds, x):
    remain = [g for g in grounds if g not in green]
    for red in combinations(remain,y):
        max_flowers = max(max_flowers, BFS(green,red))

print(max_flowers)