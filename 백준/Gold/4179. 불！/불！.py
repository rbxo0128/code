import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))

fire_stack = deque()
pos = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == "J":
            if i == 0 or i==n-1 or j==0 or j==m-1:
                print(1)
                sys.exit()

            pos.append((i,j))
            graph[i][j] = "."

        if graph[i][j] == "F":
            fire_stack.append((i,j))

directions = [(0,1),(0,-1),(1,0),(-1,0)]



def fire_move(graph, fire_stack):
    new_fire = deque()

    while fire_stack:
        x,y = fire_stack.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m and graph[sx][sy] == ".":
                graph[sx][sy] = "F"
                new_fire.append((sx,sy))

    return new_fire


def jihoon_move(graph,pos,visited):
    new_pos = deque()

    while pos:
        x,y = pos.popleft()
        visited[x][y] = True
        for dx,dy in directions:
            sx,sy = x+dx, y+dy
            if 0<=sx<n and 0<=sy<m and graph[sx][sy] == "." and not visited[sx][sy]:
                if sx == 0 or sx == n-1 or sy == 0 or sy == m-1:
                    return False

                new_pos.append((sx,sy))
                visited[sx][sy] = True

    if not new_pos:
        print("IMPOSSIBLE")
        sys.exit()

    return new_pos

visited = [[False]*m for i in range(n)]
day=1
while True:
    day+=1
    fire_stack = fire_move(graph,fire_stack)

    pos = jihoon_move(graph,pos, visited)
    if not pos:
        break

print(day)