import sys
from collections import deque

def BFS(i,j):
    queue = deque([(i,j)])

    target = graph[i][j]

    result[i][j] = "."

    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m and graph[sx][sy] == target and result[sx][sy] == "#":
                queue.append((sx,sy))
                result[sx][sy] = "."

def look_around(x,y):
    result[x][y] = "."
    for dx,dy in directions:
        sx,sy = x+dx,y+dy
        if 0<=sx<n and 0<=sy<m:
            result[sx][sy] = "."

input = sys.stdin.readline

directions = [(1,0),(-1,0),(0,1),(0,-1)]
dir_map = {"L" : (0,-1), "R" : (0,1), "U" : (-1,0), "D" : (1,0)}

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input().strip()))

x,y = map(int, input().split())
x-=1
y-=1

arr = list(input().strip())

result = [["#"] * m for i in range(n)]

for op in arr:
    if op == "W":
        if result[x][y] == "#":
            BFS(x,y)
    else:
        dx,dy = dir_map[op]
        x+=dx 
        y+=dy

look_around(x,y)

for row in result:
    print("".join(row))