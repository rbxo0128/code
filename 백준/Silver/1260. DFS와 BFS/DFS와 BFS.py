import sys
from collections import deque
from itertools import permutations


n,m,v= map(int,sys.stdin.readline().split())

graph = [[] for i in range(n)]
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

for i in range(n):
    graph[i].sort()

visited = [False for i in range(n)]

BFS_result = []
DFS_result = []

def DFS(start):
    visited[start] = True    
    DFS_result.append(start+1)

    for i in graph[start]:
        if not visited[i]:
            DFS(i)

def BFS():
    visited = [False for i in range(n)]
    visited[v-1] = True
    BFS_result.append(v)

    stack = deque()
    for i in graph[v-1]:
        stack.append(i)
        visited[i] = True
        BFS_result.append(i+1)

    while stack:
        x = stack.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                BFS_result.append(i+1)

DFS(v-1)
BFS()
print(' '.join(map(str,DFS_result)))
print(' '.join(map(str,BFS_result)))