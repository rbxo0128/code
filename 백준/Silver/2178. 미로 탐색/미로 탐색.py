from collections import deque

def DFS(graph, visited, start, num):
    visited[start-1] = True
    num.append(start)
    for i in range(len(graph[0])):
        if graph[start-1][i] == 1 and not visited[i]:
            DFS(graph,visited,i+1,num)
    
    return

def BFS(graph, visited):
    visited[0][0] = True
    count = 1
    stack = deque([(0,0,count)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n = len(graph)
    m = len(graph[0])
    while stack:
        stc = stack.popleft()
        x,y,count = stc[0],stc[1],stc[2]
        if x==len(graph)-1 and y == len(graph[0])-1:
            return count

        for dx,dy in directions:
            nx,ny = x+dx, y+dy

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1' and not visited[nx][ny]:
                stack.append((nx,ny,count+1))
                visited[nx][ny] = True


a,b = map(int, input().split())

visited = [[False]*b for i in range(a)]
graph = [[0]*b for i in range(a)]

for i in range(a):
    node = str(input())
    k = 0
    for j in node:
        graph[i][k] = j
        k+=1
num = BFS(graph,visited)
print(num)