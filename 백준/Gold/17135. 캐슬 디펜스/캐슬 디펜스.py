import sys
from itertools import combinations
from collections import deque

n,m,d = map(int, sys.stdin.readline().split())

tower = []
for i in range(n):
    tower.append(list(map(int, sys.stdin.readline().split())))

archers = [i for i in range(m)]

result = []

directions = [(0,-1),(-1,0),(0,1)]
def BFS(j, turn, check):
    global defeat

    visited = [[False] *m for i in range(n)]

    queue = deque()

    if tower[n-turn][j] == 1:
        check.append([n-turn,j])
        return
    
    visited[n-turn][j] = True
    queue.append((n-turn,j,1))

    while queue:
        x,y,cnt = queue.popleft()

        if cnt == d+1:
            return
        
        if tower[x][y] == 1:
            check.append([x,y])
            return
        
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m and not visited[sx][sy]:
                queue.append((sx,sy,cnt+1))
        
for archer in combinations(archers, 3):
    defeat = 0
    back = []
    for i in range(1,n+1):
        check = []
        for j in range(3):
            BFS(archer[j], i, check)

        for x,y in check:
            if tower[x][y] == 1:
                tower[x][y] = 0
                defeat+=1
                back.append([x,y])

    for x,y in back:
        tower[x][y] = 1

    result.append(defeat)

print(max(result))