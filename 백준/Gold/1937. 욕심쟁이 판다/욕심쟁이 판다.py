import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0] * n for i in range(n)]
directions = [(1,0),(-1,0),(0,1),(0,-1)]
def DFS(x,y):
    if dp[x][y]:
        return dp[x][y]
    
    dp[x][y] = 1
    for dx,dy in directions:
        nx,ny = x+dx, y +dy
        if 0<=nx<n and 0<=ny<n and graph[x][y] < graph[nx][ny]:
            dp[x][y] = max(dp[x][y], DFS(nx, ny) + 1)

    return dp[x][y]
    
for i in range(n):
    for j in range(n):
        DFS(i,j)

print(max(max(row) for row in dp))