import heapq
import sys


def shortest(graph,start):
    heap = []
    distances = [float('inf') for i in range(len(graph))]
    distances[start] = 0

    heapq.heappush(heap, (0,start))

    while heap:
        cur_weight, cur_node = heapq.heappop(heap)

        if cur_weight > distances[cur_node]:
            continue

        for n, w in graph[cur_node].items():
            if distances[n] > cur_weight + w:
                distances[n] = cur_weight + w
                heapq.heappush(heap, (cur_weight+w,n))

    return distances

v,e = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline())

graph = [{} for i in range(v)]
for i in range(e):
    x,y,w = map(int, sys.stdin.readline().split())
    if y-1 in graph[x-1]:
        if graph[x-1][y-1] > w:
            graph[x-1][y-1] = w
    else:
        graph[x-1][y-1] = w

for dist in shortest(graph,start-1):
    if dist == float("inf"):
        print("INF")
        continue
    print(dist)