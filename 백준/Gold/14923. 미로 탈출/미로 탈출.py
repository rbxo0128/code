import sys
from collections import deque

input = sys.stdin.readline

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def BFS():
    queue = deque()
    queue.append((hx,hy,0))
    visited[hx][hy][0] = True
    cnt = 0
    while queue:
        for i in range(len(queue)):
            x,y,k = queue.popleft()
            if x == ex and y == ey:
                return cnt
            
            for dx,dy in directions:
                sx,sy = x+dx,y+dy
                if 0<=sx<n and 0<=sy<m:
                    if graph[sx][sy] == 0 and not visited[sx][sy][k]:
                        queue.append((sx,sy,k))
                        visited[sx][sy][k] = True

                    if not k and graph[sx][sy] == 1 and not visited[sx][sy][1]:
                        queue.append((sx,sy,1))
                        visited[sx][sy][1] = True
        
        cnt += 1

    return -1

n,m = map(int, input().split())

hx,hy = map(int, input().split())
ex,ey = map(int, input().split())
hx,hy,ex,ey = hx-1,hy-1,ex-1,ey-1
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

visited = [[[False,False] for i in range(m)] for i in range(n)]

print(BFS())