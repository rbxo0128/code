import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

visited = [False] * n

max_n = 0
def DFS(level,cnt, idx):
    global max_n

    if level == n-1:
        max_n = max(max_n,cnt)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            DFS(level+1, cnt + abs(arr[idx] - arr[i]), i)
            visited[i] = False

for i in range(n):
    visited[i] = True
    DFS(0,0,i)
    visited[i] = False

print(max_n) 