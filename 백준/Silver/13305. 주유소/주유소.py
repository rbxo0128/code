import sys

n = int(sys.stdin.readline())

dist = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

    
count = 0
tmp = prices[0]
dist_sum = dist[0]
for i in range(1,len(dist)):
    if tmp < prices[i]:
        dist_sum += dist[i]
    
    else:
        count += dist_sum*tmp
        dist_sum = dist[i]
        tmp = prices[i]
    

count += tmp * dist_sum
print(count)