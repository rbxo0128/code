from itertools import combinations
from collections import deque
import sys

def BFS(graph,n,m,queue,result):
    visited = [[False] * m for _ in range(n)]
    queue2 = deque(queue[:])
    for x, y in queue2:
        visited[x][y] = True

    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue2:
        x,y = queue2.popleft()
        for sx,sy in direction:
            dx,dy = sx+x,sy+y
            if 0<=dx<n and 0<=dy<m and graph[dx][dy] == 0 and visited[dx][dy] == False:
                visited[dx][dy] = True
                queue2.append([dx,dy])
    count=0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and graph[i][j] == 0:
                count+=1
    result.append(count)

n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

wall = []
queue = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            queue.append([i,j])
        elif graph[i][j] == 0:
            wall.append([i,j])

wall_graph = combinations(wall,3)
result = []
for walls in wall_graph:
    graph[walls[0][0]][walls[0][1]] = 1
    graph[walls[1][0]][walls[1][1]] = 1
    graph[walls[2][0]][walls[2][1]] = 1
    BFS(graph,n,m,queue,result)
    graph[walls[0][0]][walls[0][1]] = 0
    graph[walls[1][0]][walls[1][1]] = 0
    graph[walls[2][0]][walls[2][1]] = 0

print(max(result))