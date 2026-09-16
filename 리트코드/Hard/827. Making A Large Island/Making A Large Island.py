from collections import deque

class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)

        board = [[0] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]

        num = 1
        answer = 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    q = deque([(i, j)])
                    visited[i][j] = True
                    blocks = [(i, j)]

                    while q:
                        x, y = q.popleft()

                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy

                            if (
                                0 <= nx < n
                                and 0 <= ny < n
                                and not visited[nx][ny]
                                and grid[nx][ny] == 1
                            ):
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                blocks.append((nx, ny))

                    size = len(blocks)
                    answer = max(answer, size)

                    for x, y in blocks:
                        board[x][y] = (num, size)

                    num += 1

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    seen = set()
                    size = 1

                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0:
                            island, cnt = board[nx][ny]

                            if island not in seen:
                                seen.add(island)
                                size += cnt

                    answer = max(answer, size)

        return answer