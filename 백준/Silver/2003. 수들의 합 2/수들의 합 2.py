import sys
    
n,m= map(int,sys.stdin.readline().split())

graph = list(map(int,sys.stdin.readline().split()))

left = 0
s = 0
ans = 0

for i in range(n):
    s += graph[i]
    
    while s >= m:
        if s == m:
            ans+=1
        s -= graph[left]
        left += 1

print(ans)