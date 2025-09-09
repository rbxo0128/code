import sys
from collections import deque

input = sys.stdin.readline

n,m,k = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

directions = [(1,0),(-1,0),(0,1),(0,-1)]
def BFS(num):
    visited = [[False] *m for i in range(n)]
    queue = deque()
    cnt = 0
    for i in range(n):
        if graph[i][0] <= num:
            queue.append((i,0))
            cnt+=1
            visited[i][0] = True

        if graph[i][m-1] <= num:
            queue.append((i,m-1))
            cnt+=1
            visited[i][m-1] = True
    
    for i in range(1,m-1):
        if graph[0][i] <= num:
            cnt+=1
            queue.append((0,i))
            visited[0][i] = True

    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            sx,sy = x+dx, y+dy
            if 0<=sx<n and 0<=sy<m and not visited[sx][sy] and graph[sx][sy] <= num:
                cnt+=1
                queue.append((sx,sy))
                visited[sx][sy] = True

    if cnt >= k:
        return True

    return False
left = 0
right = 10**6 + 1
while left + 1 < right:
    mid = (left + right) // 2 
    if BFS(mid):
        right = mid
    else:
        left = mid

print(right)