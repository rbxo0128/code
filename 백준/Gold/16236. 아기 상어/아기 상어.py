import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            shark = (i,j)
directions = [(1,0),(-1,0),(0,1),(0,-1)]
level = 2
feed = 0
time = 0

def BFS(shark):
    global feed, level,time

    visited = [[False] * n for i in range(n)]
    i,j = shark[0],shark[1]
    visited[i][j] = True
    stack = deque()
    stack.append((i,j,0))
    min_dist = -1
    result = []
    while stack:
        x,y,cnt = stack.popleft()
        if result:
            if result[0][2] < cnt:
                break

        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<n and graph[sx][sy] <= level and not visited[sx][sy]:
                stack.append((sx,sy,cnt+1))
                visited[sx][sy] = True
                if 0 < graph[sx][sy] < level:
                    result.append([sx,sy,cnt+1])
                    
    if not result:
        return shark

    result.sort(key= lambda x : (x[2],x))
    x,y,move = result[0]
    time += move
    graph[x][y] = 0
    feed += 1
    if feed == level:
        level+=1
        feed = 0

    return (x,y)

while True:
    new_shark = BFS(shark)
    if new_shark == shark:
        break

    shark = new_shark

print(time)
