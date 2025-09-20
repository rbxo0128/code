from collections import deque
def solution(board):
    graph = []
    for i in board:
        graph.append(list(i))
        
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "R":
                start = (i,j,0)
                graph[i][j] = "."
            elif graph[i][j] == "G":
                end = (i,j)
                graph[i][j] = "."
    
    directions = [(0,1),(0,-1),(-1,0),(1,0)]
    def BFS():
        queue = deque([start])
        visited =[[False] * m for i in range(n)]
        visited[start[0]][start[1]] = True
        while queue:
            x,y,cnt = queue.popleft()
            if (x,y) == end:
                return cnt
            
            for dx,dy in directions:
                sx,sy = x,y
                while True:
                    if 0<=sx+dx<n and 0<=sy+dy<m:
                        if graph[sx+dx][sy+dy] == "D":
                            if not visited[sx][sy]:
                                visited[sx][sy] = True
                                queue.append((sx,sy,cnt+1))
                            break
                        sx += dx
                        sy += dy
                    else:
                        if not visited[sx][sy]:
                            visited[sx][sy] = True
                            queue.append((sx,sy,cnt+1))
                        break
        return -1
                    
    return BFS()