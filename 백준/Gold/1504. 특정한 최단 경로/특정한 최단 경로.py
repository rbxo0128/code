import sys
def get_smallest_node(distance,visited):
  mins = float('inf')
  index = 0
  for i in range(0, n):
    if distance[i] < mins and not visited[i]: 
      mins = distance[i]
      index = i

  return index

def dijkstra(start):
    visited = [False] * (n)
    distance = [float('inf')] * (n)
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]
    
    for _ in range(n-1): 
        now = get_smallest_node(distance,visited)
        visited[now] = True

        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]]= distance[now] + j[1]

    return distance

n, m = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n)]

for i in range(m):
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u-1].append((v-1, w))
  graph[v-1].append((u-1, w))

x,y = map(int, sys.stdin.readline().split())

first = dijkstra(0)
second = dijkstra(x-1)
third = dijkstra(y-1)

answer = min(first[x-1] + second[y-1] + third[n-1],first[y-1] + third[x-1] + second[n-1])
if (answer == float('inf')):
    print(-1)
else: 
    print(min(first[x-1] + second[y-1] + third[n-1],first[y-1] + third[x-1] + second[n-1]))