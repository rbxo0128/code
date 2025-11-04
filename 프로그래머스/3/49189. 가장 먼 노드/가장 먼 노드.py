from collections import deque

def solution(n, edge):
    graph = [[] for i in range(n)]
    for i in edge:
        x,y = i[0]-1,i[1]-1
        graph[x].append(y)
        graph[y].append(x)
        
    arr = BFS(graph)
    max1 = max(arr, key=lambda x: x[1])[1]
    arr1 = [x for x in arr if x[1] == max1]
    print(arr1)
    return len(arr1)

def BFS(graph):
    visited = [False for i in range(len(graph))]
    stack = deque([[0,0]])
    arr = []
    visited[0] = True
    while stack:
        x,count = stack.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                stack.append([i,count+1])
                arr.append([i,count+1])
    return arr