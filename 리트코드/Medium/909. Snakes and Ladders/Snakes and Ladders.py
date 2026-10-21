from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        visited = [False] * n * n
        visited[0] = True

        board_new = []
        for i in range(n):
            if i % 2 == 0:
                for x in board[n-1-i]:
                    board_new.append(x)
            else:
                for j in range(n):
                    board_new.append(board[n-1-i][n-1-j])

        queue = deque()
        queue.append((0,0))
        while queue:
            x,cnt = queue.popleft()

            if x == n*n-1:
                return cnt
            go = False

            for i in range(6,0,-1):
                if x+i < n*n and board_new[x+i] == -1:
                    if not go and not visited[x+i]:
                        queue.append((x+i,cnt+1))
                        go = True
                    
                    visited[x+i] = True
                    
                else:
                    if x+i < n*n and not visited[board_new[x+i]-1]:
                        queue.append((board_new[x+i]-1,cnt+1))
                        visited[board_new[x+i]-1] = True

        return -1