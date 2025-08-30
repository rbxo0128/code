import sys

n,m = map(int, sys.stdin.readline().split())

directions = [-1,0,1]

def DFS(graph,visited, x,y):
    global answer

    visited[x][y] = True
    if y == m-1:
        answer += 1
        return True


    for dx in directions:
        sx = x+dx
        if 0<=sx<n and not visited[sx][y+1] and graph[sx][y+1] == ".":
            if DFS(graph,visited,sx,y+1):
                return True


graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))

visited = [[False] * m for i in range(n)]

answer = 0
for i in range(n):
    DFS(graph,visited,i,0)

print(answer)