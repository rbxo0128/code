import sys
from collections import deque

horse_directions = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
directions = [(1,0),(-1,0),(0,1),(0,-1)]

def BFS(graph, visited, n, m, k):
    visited[0][0][0] = True
    queue = deque()
    queue.append((0,0,0,0))
    while queue:
        x,y,cnt, horse_cnt = queue.popleft()
        if x == n-1 and y == m-1:
            return cnt
        
        if horse_cnt < k:
            for dx,dy in horse_directions:
                sx,sy = x+dx, y+dy
                if 0<= sx < n and 0<= sy < m and not visited[sx][sy][horse_cnt+1] and graph[sx][sy] == 0:
                    queue.append((sx,sy,cnt+1, horse_cnt+1))
                    visited[sx][sy][horse_cnt+1] = True
        
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<= sx < n and 0<= sy < m and not visited[sx][sy][horse_cnt] and graph[sx][sy] == 0:
                queue.append((sx,sy,cnt+1, horse_cnt))
                visited[sx][sy][horse_cnt] = True

    return -1

k = int(sys.stdin.readline())
graph = []
m,n = map(int, sys.stdin.readline().split())
visited = [[[False]*(k+1) for i in range(m)] for j in range(n)]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

print(BFS(graph,visited,n,m,k))