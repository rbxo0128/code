import sys
from collections import deque

def BFS(graph, visited,i,j, result):
    queue = deque()
    count = 1
    queue.append((i,j))
    directions = [(1,0),(-1,0),(0,-1),(0,1)]
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m and not visited[sx][sy] and graph[sx][sy] == 0:
                visited[sx][sy] = True
                count+=1
                queue.append((sx,sy))

    result.append(count)    

n,m,k = map(int, sys.stdin.readline().split())

graph = [[0]*(m) for i in range(n)]
visited = [[False]*(m) for i in range(n)]

for i in range(k):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    for x in range(y1,y2):
        for y in range(x1,x2):
            graph[x][y] = 1

result = []
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 0:
            visited[i][j] = True
            BFS(graph,visited,i,j, result)

print(len(result))
result.sort()
print(' '.join(map(str, result)))