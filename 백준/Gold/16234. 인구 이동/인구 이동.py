import sys
from collections import deque

def BFS(graph,visited,i,j,l,r):
    stack = deque()
    stack.append((i,j))
    result= []
    result.append((i,j))
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    n= len(graph)
    while stack:
        x,y = stack.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<n and not visited[sx][sy] and l<= abs(graph[x][y] - graph[sx][sy]) <=r:
                visited[sx][sy] = True
                stack.append((sx,sy))
                result.append((sx,sy))

    result_sum = 0
    result_len = len(result)
    for x,y in result:
        result_sum += graph[x][y]

    for x,y in result:
        graph[x][y] = result_sum//result_len    



n,l,r= map(int,sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

day = 0
while True:
    visited = [[False]*n for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt+=1
                visited[i][j] = True
                BFS(graph, visited, i, j, l, r)
    if cnt == n*n:
        break
    day+=1

print(day)