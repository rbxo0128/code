import sys
    
n,m= map(int,sys.stdin.readline().split())

graph = list(map(int,sys.stdin.readline().split()))

left = 0
s = 0
ans = n + 1

for i in range(n):
    s += graph[i]
    
    while s >= m:
        ans = min(ans, i - left + 1)
        s -= graph[left]
        left += 1

if ans == n+1:
    print(0)
else:
    print(ans)

