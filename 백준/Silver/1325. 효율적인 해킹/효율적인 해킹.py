import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

counts = [0] * (n + 1)
visited = [0] * (n + 1)
node = 1

for i in range(1, n + 1):
    q = deque([i])
    visited[i] = node
    cnt = 0
    while q:
        u = q.popleft()
        for v in arr[u]:
            if visited[v] != node:
                visited[v] = node
                cnt += 1
                q.append(v)
    counts[i] = cnt
    node += 1

result = []
max_cnt = max(counts)
for i in range(1,n+1):
    if counts[i] == max_cnt:
        result.append(i)
print(" ".join(map(str,result)))
