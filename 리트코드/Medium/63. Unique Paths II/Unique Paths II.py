class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        arr = []
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        arr = [[0] * m for i in range(n)]
        
        if obstacleGrid[0][0] == 1:
            return 0

        arr[0][0] = 1

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    continue

                if i > 0:
                    arr[i][j] += arr[i-1][j]

                if j > 0:
                    arr[i][j] += arr[i][j-1]

        return arr[-1][-1]