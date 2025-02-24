import sys
import heapq



n= int(sys.stdin.readline())

heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -num)