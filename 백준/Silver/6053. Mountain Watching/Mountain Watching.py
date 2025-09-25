import sys
input = sys.stdin.readline

n = int(input())
h = [int(input()) for _ in range(n)]

up = [1] * n
for i in range(1, n):
    if h[i] >= h[i-1]:
        up[i] = up[i-1] + 1

down = [1] * n
for i in range(n-2, -1, -1):
    if h[i] >= h[i+1]:
        down[i] = down[i+1] + 1

answer = 0
for i in range(n):
    width = up[i] + down[i] - 1
    if width > answer:
        answer = width

print(answer)
