import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n,m= map(int,input().split())

graph= []
viruses = []

for i in range(n):
    graph.append(list(map(int, input().split())))

cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            viruses.append((i,j))

        if graph[i][j] == 0:
            cnt+=1

if cnt == 0:
    print(0)
    exit()

directions = [(1,0),(-1,0),(0,1),(0,-1)]
result = []
def BFS(virus):
    visited = [[False] * n for i in range(n)]
    for i,j in virus:
        visited[i][j] = True

    days = 0
    check = 0

    while True:
        new_virus = deque()
        while virus:
            x,y = virus.popleft()
            for dx,dy in directions:
                sx,sy = x+dx,y+dy
                if 0<=sx<n and 0<=sy<n and not visited[sx][sy] and (graph[sx][sy] == 0 or graph[sx][sy] == 2):
                    if graph[sx][sy] == 0:
                        check += 1
                    new_virus.append((sx,sy))
                    visited[sx][sy] = True

        if check == cnt:
            return days
        
        if not new_virus:
            return float("inf")
        
        virus = new_virus
        days+=1
        

max_cnt = float("inf")
for virus in combinations(viruses, m):
    max_cnt = min(BFS(deque(virus)), max_cnt)

if max_cnt == float("inf"):
    print(-1)
else:
    print(max_cnt+1)