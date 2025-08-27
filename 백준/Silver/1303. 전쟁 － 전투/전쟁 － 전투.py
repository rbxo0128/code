import sys

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(m):
    graph.append(list(sys.stdin.readline().strip()))

black = 0
white = 0

visited = [[False] * n for i in range(m)]
directions = [(1,0),(-1,0),(0,1),(0,-1)]
cnt = 0
def DFS(x,y,visited, army):
    global black,white,cnt

    cnt+=1
    visited[x][y] = True
    for dx,dy in directions:
        sx,sy = x+dx,y+dy
        if 0<=sx<m and 0<=sy<n and not visited[sx][sy] and graph[sx][sy] == army:
            DFS(sx,sy,visited, army)



for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            cnt = 0                
            DFS(i,j,visited,graph[i][j])
            if graph[i][j] == "B":
                black += cnt*cnt
            else:
                white += cnt*cnt

print(white,black)