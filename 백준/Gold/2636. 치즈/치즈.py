import sys
from collections import deque

def BFS(graph,n,m,result):
    visited = [[False] * m for i in range(n)]
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    directions = [(1,0),(-1,0),(0,-1),(0,1)]
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m and not visited[sx][sy]:
                visited[sx][sy] = True
                if graph[sx][sy] == 0:
                    queue.append((sx,sy))
                elif graph[sx][sy] == 1:
                    graph[sx][sy] = 0

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count+=1
    result.append(count)
    if (count == 0):
        return False
    
    return True

n,m = map(int, sys.stdin.readline().split())

graph = []
visited = [[False]*(m) for i in range(n)]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count+=1
if count == 0:
    print(0)
    print(0)

else:
    result = []
    while BFS(graph,n,m,result):
        pass

    cnt = len(result)
    print(cnt)
    if cnt == 1:
        print(count)
    else:
        print(result[cnt-2])
