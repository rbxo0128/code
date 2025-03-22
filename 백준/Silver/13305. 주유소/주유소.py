import sys

n = int(sys.stdin.readline())

dist = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

    
tmp = float("inf")
count = 0
idx = 0
dist_sum = 0
for price in prices:
    if idx == len(dist):
        break
    
    if tmp < price:
        dist_sum += dist[idx]
        continue

    else:
        tmp = price
        dist_sum += dist[idx]
        count += price * dist_sum
        dist_sum = 0

    idx+=1

print(count)