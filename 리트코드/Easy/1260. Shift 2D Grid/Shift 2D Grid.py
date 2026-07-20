class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        grid_list = []
        for x in grid:
            for y in x:
                grid_list.append(y)

        k %= len(grid_list)
        if k == 0:
            return grid

        answer_list = grid_list[-k:] + grid_list[:-k]
        answer = []
        for i in range(n):
            tmp = []
            for j in range(m):
                tmp.append(answer_list[i*m+j])
            answer.append(tmp)

        return answer