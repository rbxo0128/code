import heapq
import sys

n= int(sys.stdin.readline())

for i in range(n):
    x = int(sys.stdin.readline())

    min_heap = []
    max_heap = []
    stack = {}
    count = 0
    for i in range(x):
        op, num = sys.stdin.readline().split()
        num = int(num)
        if op == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            stack[num] = stack.get(num, 0) + 1
            count += 1

        else:
            if count == 0:
                continue

            if num == 1:
                while stack.get(-max_heap[0], 0) == 0:
                    heapq.heappop(max_heap)

                if max_heap:
                    value = -heapq.heappop(max_heap)
                    stack[value] -= 1
            else:
                while stack.get(min_heap[0], 0) == 0:
                    heapq.heappop(min_heap)
                    
                if min_heap:
                    value = heapq.heappop(min_heap)
                    stack[value] -= 1
            
            count-=1

            if count == 0:
                stack = {}
                min_heap = []
                max_heap = []

    while min_heap and stack.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)

    while max_heap and stack.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)
    
    if count == 0:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))