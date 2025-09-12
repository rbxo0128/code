import sys
input = sys.stdin.readline

n = int(input())

arr = [[float("inf")] * n for i in range(n)]

for i in range(n):
    lists = list(map(int, input().split()))
    for j in range(n):
        if lists[j] == 1:
            arr[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(n):
    for j in range(n):
        if arr[i][j] == float("inf"):
            arr[i][j] = 0
        else:
            arr[i][j] = 1

for i in arr:
    print(" ".join(map(str, i)))