import sys
from collections import deque

input = sys.stdin.readline

graph = []
for i in range(12):
    graph.append(list(input().strip()))

can_queue = []
for i in range(12):
    for j in range(6):
        if graph[i][j] != ".":
            can_queue.append((i,j))

directions = [(1,0),(-1,0),(0,1),(0,-1)]
def BFS(i,j,visited):
    visited[i][j] = True
    queue = deque([(i,j)])
    history = [(i,j)]
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<12 and 0<=sy<6 and not visited[sx][sy] and graph[sx][sy] == graph[x][y]:
                queue.append((sx,sy))
                visited[sx][sy] = True
                history.append((sx,sy))

    if len(history) >= 4:
        for x,y in history:
            graph[x][y] = "."
        return True

    return False

def move(graph):
    for j in range(6):
        stack = []
        for i in range(11, -1, -1):
            if graph[i][j] != ".":
                stack.append(graph[i][j])
        for i in range(11, -1, -1):
            if stack:
                graph[i][j] = stack.pop(0)
            else:
                graph[i][j] = "."
    return graph

answer = 0
while True:
    is_puyo = False
    visited = [[False] * 6 for i in range(12)]
    for x,y in can_queue:
        if not visited[x][y] and graph[x][y] != ".":
            if BFS(x,y,visited):
                is_puyo = True
    
    if not is_puyo:
        print(answer)
        break

    graph = move(graph)
    answer += 1