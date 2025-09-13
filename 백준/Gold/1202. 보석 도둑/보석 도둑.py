import sys
import heapq

input = sys.stdin.readline

n,k = map(int, input().split())

jewels = []

for i in range(n):
    jewels.append(list(map(int, input().split())))

bags= []
for i in range(k):
    bags.append(int(input()))

jewels.sort(reverse=True)
bags.sort()

can_take = []

answer = 0
for bag in bags:
    while jewels:
        if jewels[-1][0] <= bag:
            weight, value = jewels.pop()
            heapq.heappush(can_take, -value)
        else:
            break

    if can_take:
        answer -= heapq.heappop(can_take)

print(answer)