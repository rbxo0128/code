import sys
from collections import deque

def BFS(i,j,n,m):
    global count
    visited = [[False]*m for i in range(n)]
    visited[i][j] = True
    stack = deque()
    stack.append((i,j))
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    while stack:
        x,y = stack.popleft()
        for dx,dy in direction:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<= sy <m and not visited[sx][sy] and not graph[sx][sy] == "X":
                if graph[sx][sy] == "P":
                    count+=1
                visited[sx][sy] = True
                stack.append((sx,sy))

    return count

n,m = map(int,sys.stdin.readline().split())

graph = [[]for i in range(n)]
x=0
y=0
for i in range(n):
    a = sys.stdin.readline()
    for j in range(m):
        if a[j] == 'I':
            x,y = i,j
        graph[i].append(a[j])
count = 0
answer =BFS(x,y,n,m)
if answer == 0:
    print("TT")
else:
    print(answer)