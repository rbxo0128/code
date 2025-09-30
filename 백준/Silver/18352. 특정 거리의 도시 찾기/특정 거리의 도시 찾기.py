import sys
from collections import deque

input = sys.stdin.readline

n,m,k,x = map(int, input().split())

arr =[[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)

def BFS(x):
    queue = deque([(x,0)])
    visited= [False] * (n+1)
    visited[x] = True
    answer = []
    while queue:
        node, cnt = queue.popleft()
        if cnt == k:
            answer.append(node)

        else:
            for i in arr[node]:
                if not visited[i]:
                    queue.append((i,cnt+1))
                    visited[i] = True

    return answer

answer = BFS(x)

if answer:
    answer.sort()
    for i in answer:
        print(i)

else:
    print(-1)