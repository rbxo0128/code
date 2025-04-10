import sys

n,m = map(int,sys.stdin.readline().split())

rx,ry,rd = map(int,sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

directions = [(0,1),(0,-1),(1,0),(-1,0)]
cnt = 0
visited = [[False]*m for i in range(n)]
while True:
    if not visited[rx][ry]:
        cnt+=1

    visited[rx][ry] = True
    

    isDirty = False
    for dx,dy in directions:
        sx,sy = rx+dx,ry+dy
        if graph[sx][sy] == 0 and not visited[sx][sy]:
            isDirty = True
            break

    if isDirty:
        while True:
            rd = (rd-1)%4
            if rd == 0:
                if graph[rx-1][ry] == 0 and not visited[rx-1][ry]:
                    rx-=1
                    break
            elif rd == 1:
                if graph[rx][ry+1] == 0 and not visited[rx][ry+1]:
                    ry+=1
                    break
            elif rd == 2:
                if graph[rx+1][ry] == 0 and not visited[rx+1][ry]:
                    rx+=1
                    break
            elif rd == 3:
                if graph[rx][ry-1] == 0 and not visited[rx][ry-1]:
                    ry-=1
                    break
    else:
        if rd == 0:
            if graph[rx+1][ry] == 0:
                rx+=1
            else:
                break
        elif rd == 1:
            if graph[rx][ry-1] == 0:
                ry-=1
            else:
                break
        elif rd == 2:
            if graph[rx-1][ry] == 0:
                rx-=1
            else:
                break
        elif rd == 3:
            if graph[rx][ry+1] == 0:
                ry+=1
            else:
                break

print(cnt)