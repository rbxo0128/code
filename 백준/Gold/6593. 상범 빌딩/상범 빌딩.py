import sys
from collections import deque

input = sys.stdin.readline

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def BFS(start):
    k,i,j = start
    queue = deque()
    queue.append((k,i,j,0))
    visited[k][i][j] = True
    while queue:
        floor, x,y,cnt = queue.popleft()
        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<m and not visited[floor][sx][sy]:
                if building[floor][sx][sy] == "E":
                    return cnt + 1
                
                elif building[floor][sx][sy] == ".":
                    queue.append((floor,sx,sy,cnt+1))
                    visited[floor][sx][sy] = True

        if 0<=floor+1<f and not visited[floor+1][x][y]:
            if building[floor+1][x][y] == "E":
                return cnt + 1
            
            elif building[floor+1][x][y] == ".":
                queue.append((floor+1,x,y,cnt+1))
                visited[floor+1][x][y] = True

        if 0<=floor-1<f and not visited[floor-1][x][y]:
            if building[floor-1][x][y] == "E":
                return cnt + 1
            
            elif building[floor-1][x][y] == ".":
                queue.append((floor-1,x,y,cnt+1))
                visited[floor-1][x][y] = True

    return -1


while True:
    f,n,m= map(int,input().split())

    if f == 0 and n == 0 and m == 0:
        break

    building = []

    for i in range(f):
        floor = []
        for j in range(n):
            floor.append(list(input().strip()))
        input()
        building.append(floor)

    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(f)]

    for k in range(f):
        for i in range(n):
            for j in range(m):
                if building[k][i][j] == "S":
                    start = (k,i,j)
                    building[k][i][j] = "."


    minute = BFS(start)

    if minute == -1:
        print("Trapped!")

    else:
        print("Escaped in " + str(minute) + " minute(s).")