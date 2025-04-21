import sys
sys.setrecursionlimit(10**6)
def DFS(graph,visited,x):
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            DFS(graph,visited,i)

n,m= map(int,sys.stdin.readline().split())
graph=[[] for i in range(n)]

for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

visited = [False for i in range(n)]

count=0

for i in range(n):
    if not visited[i]:
        visited[i] = True
        DFS(graph,visited,i)
        count+=1

print(count)