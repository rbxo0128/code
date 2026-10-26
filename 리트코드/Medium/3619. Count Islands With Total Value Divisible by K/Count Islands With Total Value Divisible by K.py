from collections import deque

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False]*m for i in range(n)]
        answer = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def BFS(i,j):
            nonlocal answer
            queue = deque()
            queue.append((i,j))
            visited[i][j] = True

            total = 0
            while queue:
                x,y = queue.popleft()
                total += grid[x][y]
                for dx,dy in directions:
                    sx,sy = x+dx,y+dy
                    if 0<=sx<n and 0<=sy<m and grid[sx][sy] > 0 and not visited[sx][sy]:
                        queue.append((sx,sy))
                        visited[sx][sy] = True

            if total % k == 0:
                answer += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and not visited[i][j]:
                    BFS(i,j)

        return answer