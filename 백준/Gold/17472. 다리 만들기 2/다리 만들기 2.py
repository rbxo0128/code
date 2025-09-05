import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

islands = deque()
visited = [[False] * m for i in range(n)]


directions = [(1,0),(-1,0),(0,1),(0,-1)]
def BFS(graph, visited, i,j,idx,islands):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    islands.append((i,j,idx,0,0))
    islands.append((i,j,idx,0,1))
    islands.append((i,j,idx,0,2))
    islands.append((i,j,idx,0,3))
    graph[i][j] = idx
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            sx,sy = x+dx, y+dy
            if 0<=sx<n and 0<=sy<m and not visited[sx][sy] and graph[sx][sy]==1:
                visited[sx][sy]=True
                queue.append((sx,sy))
                graph[sx][sy] = idx
                islands.append((sx,sy,idx, 0,0))
                islands.append((sx,sy,idx, 0,1))
                islands.append((sx,sy,idx, 0,2))
                islands.append((sx,sy,idx, 0,3))


idx = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            BFS(graph,visited,i,j,idx,islands)
            idx+=1

dist = []
while True:
    new_islands = deque()
    while islands:
        x,y,island,cnt,pos = islands.popleft()            
        dx,dy = directions[pos]
        sx,sy = x+dx,y+dy
        if 0<=sx<n and 0<=sy<m:
            if graph[sx][sy] == 0:
                new_islands.append((sx,sy,island,cnt+1,pos))
            
            elif not graph[sx][sy] == 0 and not island == graph[sx][sy] and cnt > 1:
                dist.append([island, graph[sx][sy], cnt])
        
    islands = new_islands

    if not islands:
        break

parents = {}
answer = 0
def find(x):
    if x not in parents:
        parents[x] = x

    if parents[x] != x:
        parents[x] = find(parents[x])

    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if find(a) != find(b):
        parents[a] = b

dist.sort(key= lambda x:x[2])
for x,y,w in dist:
    if find(x) != find(y):
        union(x,y)
        answer += w

roots = set(find(i) for i in range(1, idx))

if len(roots) == 1:
    print(answer)
else:
    print(-1)