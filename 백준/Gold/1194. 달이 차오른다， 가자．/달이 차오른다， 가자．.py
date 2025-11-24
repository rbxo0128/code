import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input().strip()))

visited = [[[False] * 64 for i in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == "0":
            start_x,start_y = i,j
            graph[i][j] = "."

directions = [(1,0),(-1,0),(0,1),(0,-1)]
keys = ["a","b","c","d","e","f"]
doors = ["A","B","C","D","E","F"]

def BFS(i,j):
    queue = deque()
    queue.append((i,j,0,0))
    visited[i][j][0] = True
    while queue:
        x,y,k,cnt = queue.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m and not visited[sx][sy][k] and graph[sx][sy] != "#":
                if graph[sx][sy] == ".":
                    queue.append((sx,sy,k,cnt+1))
                    visited[sx][sy][k] = True

                elif graph[sx][sy] == "1":
                    return cnt+1
                
                elif graph[sx][sy] in keys:
                    key = 1 << keys.index(graph[sx][sy])
                    new_key = k | key
                    if not visited[sx][sy][new_key]:
                        queue.append((sx,sy,new_key,cnt+1))
                        visited[sx][sy][new_key] = True

                elif graph[sx][sy] in doors:
                    if k & (1 << doors.index(graph[sx][sy])):
                        queue.append((sx,sy,k,cnt+1))
                        visited[sx][sy][k] = True

    return -1

print(BFS(start_x,start_y))