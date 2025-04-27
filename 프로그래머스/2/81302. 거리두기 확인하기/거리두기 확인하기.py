from collections import deque

def solution(places):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    def BFS(i,j,visited,result, place):
        stack = deque()
        visited[i][j] = True
        stack.append((i,j,0))
        while stack:
            x,y,cnt = stack.popleft()
                
            for dx,dy in directions:
                sx,sy = x+dx,y+dy
                if 0<= sx < 5 and 0<= sy < 5 and not visited[sx][sy]:
                    if place[sx][sy] == "O":
                        stack.append((sx,sy,cnt+1))
                        visited[sx][sy] = True

                    elif place[sx][sy] == "P":
                        if cnt <= 1:
                            result.append(0)
                            return True
                        
        return False
            
            
            
    
    result = []
    for place in places:
        stack = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    stack.append((i,j))

        visited = [[False]*5 for i in range(5)]
        plus = True
        for x,y in stack:
            if BFS(x,y,visited,result,place):
                plus = False
                break
        if plus:
            result.append(1)
                
    return result