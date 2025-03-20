import sys
from collections import deque
from itertools import permutations

def BFS(graph, visited, i,j,idx,result):
    global cnt
    visited[i][j] = True
    stack = deque()
    graph[i][j] = idx
    stack.append((i,j))
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    while stack:
        x,y = stack.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<= nx< n and 0<= ny<n and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = idx
                stack.append((nx,ny))
                cnt+=1

    result.append(cnt)

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

visited = [[False]*n for i in range(n)]

idx = 1
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt=1
            BFS(graph,visited,i,j,idx,result)
            idx+=1

print(idx-1)
result.sort()
for i in result:
    print(i)

