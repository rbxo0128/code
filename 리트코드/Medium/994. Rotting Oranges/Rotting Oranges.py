from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        visited = [[False] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    visited[i][j] = True
                    queue.append((i,j))
        answer = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            new_queue = deque()
            for i in range(len(queue)):
                x,y = queue.popleft()
                for dx,dy in directions:
                    sx,sy = x+dx,y+dy
                    if 0<=sx<n and 0<=sy<m and grid[sx][sy] == 1 and not visited[sx][sy]:
                        new_queue.append((sx,sy))
                        visited[sx][sy] = True

            if not new_queue:
                break

            answer += 1
            queue = new_queue

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    return -1

        return answer
