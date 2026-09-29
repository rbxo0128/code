from collections import deque

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == ")" or grid[n-1][m-1] == "(":
            return False

        queue = deque()
        queue.append((0,0,1))

        visited = set()

        directions = [(1,0),(0,1)]
        while queue:
            x,y,cnt = queue.popleft()
            
            if x == n-1 and y == m-1 and cnt == 0:
                return True

            for dx,dy in directions:
                sx,sy = x+dx,y+dy
                if 0<=sx<n and 0<=sy<m:
                    if grid[sx][sy] =="(" and not (sx,sy,cnt + 1) in visited:
                        queue.append((sx,sy,cnt+1))
                        visited.add((sx,sy,cnt+1))

                    elif grid[sx][sy] == ")" and cnt > 0 and not (sx,sy,cnt-1) in visited:
                        queue.append((sx,sy,cnt-1))
                        visited.add((sx,sy,cnt-1))
                        
        return False