import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n,m,k= map(int,input().split())

graph= []

for i in range(n):
    graph.append(list(map(int, input().strip())))

directions = [(1,0),(-1,0),(0,1),(0,-1)]

visited = [[[False] * (k+1) for i in range(m)] for i in range(n)]

def BFS():
    queue = deque()
    queue.append((0,0,1,0))

    while queue:
        visited[0][0][0] = True
        x,y,cnt,k_cnt = queue.popleft()

        if x == n-1 and y == m-1:
            return cnt

        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m:
                if not visited[sx][sy][k_cnt] and graph[sx][sy] == 0:
                    visited[sx][sy][k_cnt] = True
                    queue.append((sx,sy,cnt+1,k_cnt))

                if k_cnt < k and not visited[sx][sy][k_cnt+1] and graph[sx][sy] == 1:
                    visited[sx][sy][k_cnt+1] = True
                    queue.append((sx,sy,cnt+1,k_cnt+1))

    return -1
        
print(BFS())