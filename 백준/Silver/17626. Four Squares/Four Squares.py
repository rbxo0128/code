import sys
import math
from collections import deque

input = sys.stdin.readline

n = int(input())

squares = [i*i for i in range(1, int(math.sqrt(n)) + 1)]

cnt = 0
queue = deque()
queue.append((0,0))
visited = [False for i in range(n+1)]
visited[0] = True
while queue:
    x,cnt = queue.popleft()

    if x == n:
        print(cnt)
        break

    for sq in squares:
        if x + sq <= n and not visited[x+sq]:
            queue.append((x+sq,cnt+1))
            visited[x+sq] = True