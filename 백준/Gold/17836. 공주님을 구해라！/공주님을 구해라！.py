import sys
from collections import deque

input = sys.stdin.readline

n,m,t = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

directions = [(0,1),(0,-1),(1,0),(-1,0)]
def BFS():
    visited = [[False] * m for i in range(n)]
    queue = deque()
    queue.append((0,0,0))
    visited[0][0] = True
    sword = None
    while queue:
        x,y,cnt = queue.popleft()
        if cnt > t:
            break
            
        if x == n-1 and y == m-1:
            if sword:
                return min(sword, cnt)
            
            return cnt
        
        for dx,dy in directions:
            sx,sy = x+dx, y+dy
            if 0<=sx<n and 0<=sy<m and not visited[sx][sy]:
                if graph[sx][sy] == 0:
                    visited[sx][sy] = True
                    queue.append((sx,sy,cnt+1))
                elif graph[sx][sy] == 2:
                    visited[sx][sy] = True
                    sword = abs(sx-n+1) + abs(sy-m+1) + cnt + 1

    if sword:
        if sword <= t:
            return sword
    return "Fail"

print(BFS())
