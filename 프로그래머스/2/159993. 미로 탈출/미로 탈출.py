from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    graph = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                x,y = i,j
    
    return BFS(x,y,maps,n,m)

def BFS(i,j,maps,n,m):
    visited = [[False]*m for i in range(n)]
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    visited[i][j] = True
    stack = deque()
    stack.append((i,j,0))
    while stack:
        x,y,count = stack.popleft()
        for dx,dy in direction:
            sx,sy = x+dx, y+dy
            if 0<=sx<n and 0<=sy<m and not visited[sx][sy]:
                if not maps[sx][sy] == "X":
                    if maps[sx][sy] == "L":
                        answer = BFS_clicked(sx,sy,maps,n,m, count+1)
                        return answer  
                    visited[sx][sy] = True
                    stack.append((sx,sy,count+1))
                              
    return -1

def BFS_clicked(i,j,maps,n,m,count):
    visited = [[False]*m for i in range(n)]
    visited[i][j] = True
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    stack = deque()
    stack.append((i,j,count))
    while stack:
        x,y,count = stack.popleft()
        for dx,dy in direction:
            sx,sy = x+dx, y+dy
            if 0<=sx<n and 0<=sy<m and not visited[sx][sy]:
                if not maps[sx][sy] == "X":
                    if maps[sx][sy] == "E":
                        return count+1 
                    visited[sx][sy] = True
                    stack.append((sx,sy,count+1))
            
    return -1