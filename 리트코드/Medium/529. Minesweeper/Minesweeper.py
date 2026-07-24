from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n = len(board)
        m = len(board[0])

        cx,cy = click
        if board[cx][cy] == "M":
            board[cx][cy] = "X"
            return board

        visited =[[False] * m for i in range(n)]
        visited[cx][cy] = True
        check_x = [-1,0,1]
        check_y = [-1,0,1]

        queue = deque([(cx,cy)])
        while queue:
            x,y = queue.popleft()
            cnt = 0
            for dx in check_x:
                for dy in check_y:
                    sx,sy = x+dx,y+dy
                    if 0<=sx<n and 0<=sy<m:
                        if board[sx][sy] == "M":
                            cnt += 1

            if cnt == 0:
                board[x][y] = "B"
                for dx in check_x:
                    for dy in check_y:
                        sx,sy = x+dx,y+dy
                        if 0<=sx<n and 0<=sy<m and not visited[sx][sy] and board[sx][sy] == "E":
                            queue.append((sx,sy))
                            visited[sx][sy] = True
            
            else:
                board[x][y] = str(cnt)

        return board