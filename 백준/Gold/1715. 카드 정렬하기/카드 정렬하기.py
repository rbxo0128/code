import heapq
import sys

n = int(sys.stdin.readline())

heap = []
for i in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

count = 0
while len(heap) != 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    count += x+y
    heapq.heappush(heap, x+y)

print(count)