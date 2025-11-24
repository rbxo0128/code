import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n,m,k= map(int,input().split())

graph= []

for i in range(n):
    graph.append(list(map(int, input().strip())))

directions = [(1,0),(-1,0),(0,1),(0,-1)]

visited = [[[False for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

def BFS():
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = True
    night = False
    cnt = 1

    while queue:
        for i in range(len(queue)):
            x,y,k_cnt = queue.popleft()
            wait = False

            if x == n-1 and y == m-1:
                return cnt

            for dx,dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m:
                    if graph[nx][ny] == 0 and not visited[nx][ny][k_cnt]:
                        visited[nx][ny][k_cnt] = True
                        queue.append((nx, ny, k_cnt))

                    elif graph[nx][ny] == 1 and k_cnt < k:
                        if not night and not visited[nx][ny][k_cnt+1]:
                            visited[nx][ny][k_cnt+1] = True
                            queue.append((nx, ny, k_cnt+1))

                        if night:
                            wait = True

            if wait:
                queue.append((x,y,k_cnt))
            
        night = not night
        cnt += 1
    return -1
        
print(BFS())