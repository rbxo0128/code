import sys
from collections import deque

input = sys.stdin.readline

n,m= map(int,input().split())


graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

queue = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            queue.append((graph[i][j],i,j))

queue.sort()
queue = deque(queue)

s,nx,ny= map(int,input().split())
directions = [(1,0),(-1,0),(0,1),(0,-1)]
def BFS(queue):
    new_queue = deque()
    while queue:
        virus,x,y = queue.popleft()

        for dx,dy in directions:
            sx,sy = x+dx, y+dy
            if 0<= sx < n and 0<= sy < n and graph[sx][sy] == 0:
                graph[sx][sy] = virus
                new_queue.append((virus,sx,sy))

    return new_queue
for i in range(s):
    queue = BFS(queue)
    if not queue:
        break

print(graph[nx-1][ny-1])