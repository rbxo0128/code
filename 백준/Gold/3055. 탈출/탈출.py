import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))

go_visited = [[False] * m for i in range(n)]
water_visited = [[False] * m for i in range(n)]

directions = [(1,0),(-1,0),(0,1),(0,-1)]

waters = deque()
gos = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == "*":
            water_visited[i][j] = True
            waters.append((i,j))
        elif graph[i][j] == "S":
            go_visited[i][j] = True
            graph[i][j] = "."
            gos.append((i,j,0))

while True:
    new_waters = deque()
    new_gos = deque()

    while waters:
        x,y = waters.popleft()
        for dx,dy in directions:
            sx,sy = x+dx, y+dy
            if 0<=sx<n and 0<=sy<m and not water_visited[sx][sy] and graph[sx][sy] == ".":
                water_visited[sx][sy] = True
                new_waters.append((sx,sy))

    while gos:
        x,y,cnt = gos.popleft()
        for dx,dy in directions:
            sx,sy = x+dx, y+dy
            if 0<=sx<n and 0<=sy<m and not water_visited[sx][sy] and not go_visited[sx][sy]:
                if graph[sx][sy] == ".":
                    go_visited[sx][sy] = True
                    new_gos.append((sx,sy,cnt+1))

                elif graph[sx][sy] == "D":
                    print(cnt+1)
                    exit()

    gos = new_gos
    waters = new_waters

    if not gos:
        print("KAKTUS")
        exit()
