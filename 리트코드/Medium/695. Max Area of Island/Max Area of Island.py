from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        answer = 0
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for i in range(n)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visited[i][j]:
                    queue = deque()
                    queue.append((i,j))
                    cnt = 0
                    visited[i][j] = True

                    while queue:
                        x,y = queue.popleft()
                        cnt += 1
                        for dx,dy in directions:
                            sx,sy = x+dx, y+dy
                            if 0<=sx<n and 0<=sy<m and grid[sx][sy] and not visited[sx][sy]:
                                queue.append((sx,sy))
                                visited[sx][sy] = True

                    answer = max(answer,cnt)

        print(grid, visited)
        return answer