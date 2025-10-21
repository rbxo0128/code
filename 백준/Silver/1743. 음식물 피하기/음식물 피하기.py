import sys
from collections import deque

input = sys.stdin.readline

n,m,k = map(int, input().split())

trash = set()

directions = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(k):
    x,y = map(int, input().split())
    trash.add((x,y))

visited = set()

result = []
for i,j in trash:
    cnt = 0
    if (i,j) not in visited:
        queue = deque([(i,j)])
        visited.add((i,j))
        while queue:
            x,y = queue.popleft()
            cnt += 1
            for dx,dy in directions:
                sx,sy = x+dx,y+dy
                if (sx,sy) in trash and not (sx,sy) in visited:
                    queue.append((sx,sy))
                    visited.add((sx,sy))

    result.append(cnt)

print(max(result))