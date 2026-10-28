class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        dp = [[set() for i in range(m)] for i in range(n)]
        dp[0][0].add(grid[0][0])

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue

                if i > 0:
                    for x in dp[i-1][j]:
                        dp[i][j].add(x ^ grid[i][j])

                if j > 0:
                    for x in dp[i][j-1]:
                        dp[i][j].add(x ^ grid[i][j])

        return min(dp[n-1][m-1])