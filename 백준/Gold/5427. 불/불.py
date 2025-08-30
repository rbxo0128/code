import sys
from collections import deque

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def fire(graph, fires):
    new_fires = deque()
    while fires:
        x,y = fires.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m and graph[sx][sy] == ".":
                graph[sx][sy] = "*"
                new_fires.append((sx,sy))

    return new_fires

def move(graph, visited, queue):
    new_queue = deque()    
    while queue:
        x,y,cnt = queue.popleft()
        if x == n-1 or y == m-1 or x == 0 or y == 0:
            print(cnt)
            return None
        
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<= sx < n and 0<= sy < m and not visited[sx][sy] and graph[sx][sy] == ".":
                new_queue.append((sx,sy,cnt+1))
                visited[sx][sy] = True

    if not new_queue:
        print("IMPOSSIBLE")

    return new_queue

t = int(sys.stdin.readline())

for i in range(t):
    graph = []
    m,n = map(int, sys.stdin.readline().split())
    visited = [[False]*m for i in range(n)]

    for i in range(n):
        graph.append(list(sys.stdin.readline().strip()))

    fires = deque()
    
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "*":
                fires.append((i,j))
            
            elif graph[i][j] == "@":
                graph[i][j] = "."
                visited[i][j] = True
                queue.append((i,j,1)) 

    while True:
        fires = fire(graph, fires)
        queue = move(graph,visited, queue)

        if not queue:
            break