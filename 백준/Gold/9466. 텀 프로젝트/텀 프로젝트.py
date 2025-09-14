import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + [x for x in list(map(int, input().split()))]

    visited = [0] * (n+1)
    cnt = 0

    for i in range(1,n+1):
        if visited[i] == 0:
            cycle = []
            cur = i

            while visited[cur] == 0:
                visited[cur] = -1
                cycle.append(cur)
                cur = arr[cur]

            if visited[cur] == -1:
                try:
                    start = cycle.index(cur)
                    cnt += len(cycle) - start
                except ValueError:
                    pass

            for j in cycle:
                visited[j] = 1

    print(n - cnt)