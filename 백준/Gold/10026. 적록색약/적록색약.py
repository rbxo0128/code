import sys
sys.setrecursionlimit(10**6)
def DFS(graph,visited, i, j):
    if visited[i][j] == True:
        return True
    
    visited[i][j] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx,dy in directions:
        nx,ny = i+dx, j+dy
        if 0<=nx<len(graph) and 0<=ny<len(graph):
            if graph[nx][ny] == graph[i][j] and not visited[nx][ny]:
                DFS(graph,visited,nx,ny)
    
    return False    

a = int(input())

graph =[[0]*a for i in range(a)]
visited =[[False]*a for i in range(a)]
visited_G =[[False]*a for i in range(a)]
for i in range(a):
    x = input()
    for j in range(a):
        graph[i][j] = x[j]

count=0
for i in range(a):
    for j in range(a):
        if not DFS(graph,visited,i,j):
            count+=1

graph_G=graph[:]

for i in range(a):
    for j in range(a):
        if graph_G[i][j] == "G" or graph_G[i][j] == "R":
            graph_G[i][j] ="W"

count_G=0
for i in range(a):
    for j in range(a):
        if not DFS(graph_G,visited_G,i,j):
            count_G+=1

print(count,count_G)
