import sys
from collections import deque
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n,m = map(int,input().split())

board = []

for i in range(n):
    board.append(list(input().strip()))

dp = [[0] * m for i in range(n)]
visited = [[False] * m for i in range(n)]
directions = [(1,0),(-1,0),(0,1),(0,-1)]

def DFS(x,y):
    if dp[x][y]:
        return dp[x][y]

    visited[x][y] = True
    move = int(board[x][y])
    max_cnt = 0

    for dx, dy in directions:
        sx = x+dx * move
        sy = y+dy * move

        if not (0<=sx<n and 0<=sy<m):
            continue
        if board[sx][sy] == "H":
            continue
        if visited[sx][sy]:
            return float("inf")

        result = DFS(sx, sy)
        if result == float("inf"):
            return result

        max_cnt = max(max_cnt, result)

    visited[x][y] = False
    dp[x][y] = max_cnt + 1
    return dp[x][y]

result = DFS(0,0)

if result == float("inf"):
    print(-1)
else:
    print(result)