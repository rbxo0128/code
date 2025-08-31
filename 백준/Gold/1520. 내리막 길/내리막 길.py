import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

directions = [(1,0),(-1,0),(0,1),(0,-1)]

dp = [[-1] * m for _ in range(n)]

def DFS(x, y):
    if x == n-1 and y == m-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    
    for dx, dy in directions:
        sx, sy = x+dx, y+dy
        if 0 <= sx < n and 0 <= sy < m and graph[x][y] > graph[sx][sy]:
            dp[x][y] += DFS(sx, sy)
    
    return dp[x][y]

print(DFS(0, 0))