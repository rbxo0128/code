import sys
import heapq

def dijsktra(graph, n,start,end):
    dist = [float("inf") for i in range(n)]
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        weight, cur = heapq.heappop(heap)
        if weight > dist[cur]:
            continue

        for x,y in graph[cur]:
            if dist[x] > weight + y:
                dist[x] = weight + y
                heapq.heappush(heap, (dist[x],x))

    return dist[end]

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n)]
for i in range(m):
    x,y,w = map(int,sys.stdin.readline().split())
    graph[x-1].append((y-1,w))

start, end = map(int,sys.stdin.readline().split())
print(dijsktra(graph,n,start-1,end-1))