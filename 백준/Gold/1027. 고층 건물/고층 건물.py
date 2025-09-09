import sys

input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

def check(i, j):
    if i < j:
        for k in range(i+1, j):
            if h[k] * (j - i) >= h[i] * (j - i) + (h[j] - h[i]) * (k - i):
                return False
    else:
        for k in range(i-1, j, -1):
            if h[k] * (i - j) >= h[i] * (i - j) + (h[j] - h[i]) * (i - k):
                return False
    return True

max_cnt = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j and check(i, j):
            cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
