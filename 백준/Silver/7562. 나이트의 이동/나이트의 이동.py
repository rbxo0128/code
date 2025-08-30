import sys
from collections import deque

t = int(sys.stdin.readline())

directions = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

def BFS(graph, visited,x1,y1, x2, y2, n):
    visited[x1][y1] = True
    queue = deque()
    queue.append((x1,y1,0))
    while queue:
        x,y,cnt = queue.popleft()
        if x == x2 and y == y2:
            return cnt
        
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<= sx < n and 0<= sy < n and not visited[sx][sy]:
                queue.append((sx,sy,cnt+1))
                visited[sx][sy] = True

for i in range(t):
    n = int(sys.stdin.readline())
    graph = [[0] * n for i in range(n)]
    visited = [[False] * n for i in range(n)]
    x1,y1 = map(int, sys.stdin.readline().split())
    x2,y2 = map(int, sys.stdin.readline().split())
    print(BFS(graph, visited, x1,y1, x2,y2,n))
