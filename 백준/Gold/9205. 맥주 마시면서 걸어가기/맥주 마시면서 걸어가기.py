import sys
from collections import deque

t = int(sys.stdin.readline())

def BFS(graph, i,j,n):
    visited = [False for i in range(n)]
    stack = deque()
    stack.append((i,j))

    while stack:
        x,y = stack.popleft()
        if abs(graph[n+1][0] - x) + abs(graph[n+1][1] - y) <= 1000:
            return True

        for i in range(1,n+1):
            if abs(graph[i][0] - x) + abs(graph[i][1] - y) <= 1000 and not visited[i-1]:
                stack.append((graph[i][0], graph[i][1]))
                visited[i-1] = True

    return False
for i in range(t):
    n = int(sys.stdin.readline())
    graph = []
    for i in range(n+2):
        graph.append(list(map(int,sys.stdin.readline().split())))


    if BFS(graph, graph[0][0], graph[0][1],n):
        print("happy")
    else:
        print("sad")
