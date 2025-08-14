import sys

n, m= map(int,sys.stdin.readline().split())

graph = list(map(int,sys.stdin.readline().split()))

rain = 0
for i in range(1,n+1):
    start = False
    for j in range(m):
        if graph[j] >= i:
            if not start:
                start = True
                cnt = 0

            else:
                rain += cnt
                cnt = 0

        
        if graph[j] < i and start:
            cnt += 1

print(rain)