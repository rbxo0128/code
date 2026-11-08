from collections import deque

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for i in range(n)]
        def BFS(i,j):
            queue = deque()
            queue.append((i,j))
            visited[i][j] = True
            cnt = 0
            while queue:
                x,y = queue.popleft()
                cnt += 1
                for sy in range(m):
                    if grid[x][sy] == 1 and not visited[x][sy]:
                        queue.append((x, sy))
                        visited[x][sy] = True

                for sx in range(n):
                    if grid[sx][y] == 1 and not visited[sx][y]:
                        queue.append((sx, y))
                        visited[sx][y] = True

            return cnt if not cnt == 1 else 0

        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    answer += BFS(i,j)

        return answer