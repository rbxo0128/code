from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for i in range(n)]
    for i in roads:
        x,y = i[0]-1,i[1]-1
        graph[x].append(y)
        graph[y].append(x)
    
    arr=BFS(graph,destination-1)
    answer=[]
    for i in sources:
        answer.append(arr[i-1])
        
    return answer

def BFS(graph, dest):
    stack = deque([dest])
    dist = [-1 for i in range(len(graph))]
    dist[dest] = 0
    while stack:
        x = stack.popleft()
        for i in graph[x]:
            if dist[i] == -1:
                dist[i] = dist[x]+1
                stack.append(i)
                
    return dist