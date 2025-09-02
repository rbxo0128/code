from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0]*102 for i in range(102)]
    
    for x1,y1,x2,y2 in rectangle:
        for x in range(2*x1, 2*x2+1):
            for y in range(2*y1, 2*y2+1):
                    graph[x][y] = 1
    
    check_directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    stack = deque()
    stack.append((characterX*2,characterY*2,0))
    visited = [[False]*102 for i in range(102)]
    visited[characterX*2][characterY*2] = True
    while stack:
        x,y,cnt = stack.popleft()
        
        if x == itemX*2 and y == itemY*2:
            return cnt // 2
        
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<= sx<102 and 0<= sy < 102:
                if graph[sx][sy] == 1 and not visited[sx][sy]:
                    for dx1, dy1 in check_directions:
                        if 0<= sx+dx1 < 102 and 0<= sy+dy1<102 and graph[sx+dx1][sy+dy1] == 0:
                            visited[sx][sy] = True
                            stack.append((sx,sy,cnt+1))
                            break