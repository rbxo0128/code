from collections import deque

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for i in range(n)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def BFS(i,j):
            queue = deque()
            queue.append((i,j))
            visited[i][j] = True

            while queue:
                x,y = queue.popleft()
                for dx,dy in directions:
                    sx,sy = x+dx,y+dy
                    if 0<=sx<n and 0<=sy<m and grid[sx][sy] == 0 and not visited[sx][sy]:
                        queue.append((sx,sy))
                        visited[sx][sy] = True

        for i in range(n):
            if grid[i][0] == 0 and not visited[i][0]:
                BFS(i,0)
            if grid[i][m-1] == 0 and not visited[i][m-1]:
                BFS(i,m-1)
        for j in range(m):
            if grid[0][j] == 0 and not visited[0][j]:
                BFS(0,j)
            if grid[n-1][j] == 0 and not visited[n-1][j]:
                BFS(n-1,j)

        answer = 0
        for i in range(1,n-1):
            for j in range(1,m-1):
                if grid[i][j] == 0 and not visited[i][j]:
                    BFS(i,j)
                    answer += 1

        return answer