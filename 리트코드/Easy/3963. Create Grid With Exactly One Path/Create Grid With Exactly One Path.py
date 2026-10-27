import random

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#"] * n for i in range(m)]

        x,y = 0,0
        grid[0][0] = "."

        moves = [(1,0),(0,1)]
        while x < m-1 or y < n-1:
            dx, dy = random.choice(moves)

            if x + dx < m and y + dy < n:
                x += dx
                y += dy
                grid[x][y] = "."
            else:
                x+=dy
                y+=dx
                grid[x][y] = "."

        return ["".join(x) for x in grid]