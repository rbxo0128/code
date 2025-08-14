import sys
from collections import deque

n, m, oils= map(int,sys.stdin.readline().split())

maps = []
for i in range(n):
    maps.append(list(map(int,sys.stdin.readline().split())))

taxi_x, taxi_y = map(int,sys.stdin.readline().split())
taxi_x -= 1
taxi_y -= 1

customers = {}
for i in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    customers[x1-1,y1-1] = [x2-1,y2-1]

directions = [(0,1),(0,-1),(1,0),(-1,0)]

def BFS(i,j):
    global oils
    visited = [[False] * n for i in range(n)]
    queue = deque()
    queue.append((i,j,0))
    customer = []
    ismove = float("inf")
    visited[i][j] = True

    while queue:
        x,y,moves = queue.popleft()
        
        if moves > oils:
            print(-1)
            exit()

        if moves > ismove:
            break

        if (x,y) in customers:
            customer.append([x,y,customers[x,y][0],customers[x,y][1]])
            ismove = moves
            continue

        if ismove == moves:
            continue

        for dx,dy in directions:
            sx,sy = x+dx, y+dy
            if 0<=sx<n and 0<=sy<n and not visited[sx][sy] and maps[sx][sy] == 0:
                queue.append((sx,sy,moves+1))
                visited[sx][sy] = True

    if customer:
        customer.sort()
        oils -= ismove
        cx1,cy1,cx2,cy2 = customer[0]
        del customers[cx1,cy1]

        visited = [[False] * n for i in range(n)]
        queue = deque()
        queue.append((cx1,cy1,0))
        while queue:
            x,y,moves = queue.popleft()
            if moves > oils:
                print(-1)
                exit()

            if x == cx2 and y == cy2:
                oils += moves
                return x,y

            for dx,dy in directions:
                sx,sy = x+dx, y+dy
                if 0<=sx<n and 0<=sy<n and not visited[sx][sy] and maps[sx][sy] == 0:
                    queue.append((sx,sy,moves+1))
                    visited[sx][sy] = True

    else:
        print(-1)
        exit()

    print(-1)
    exit()

cnt = 0
while oils:
    taxi_x,taxi_y = BFS(taxi_x,taxi_y)
    cnt+=1
    if cnt == m:
        break

print(oils)