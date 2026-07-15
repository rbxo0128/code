from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for i in range(n)]
        queue = deque()
        queue.append((0,0,1))
        visited[0][0] = True

        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        while queue:
            x,y,cnt = queue.popleft()
            if x == n-1 and y == m-1:
                return cnt

            for dx,dy in directions:
                sx,sy = x+dx,y+dy
                if 0 <= sx < n and 0 <= sy < m and not visited[sx][sy] and grid[sx][sy] == 0:
                    visited[sx][sy] = True
                    queue.append((sx,sy,cnt+1))

        return -1