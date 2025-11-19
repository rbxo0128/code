import sys

input = sys.stdin.readline

n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

left = max(arr)
right = sum(arr) + 1

while left < right:
    mid = (left+right) // 2
    total = mid
    cnt = 1
    for p in arr:
        if total < p:
            cnt += 1
            total = mid

        total -= p

    if cnt > m:
        left = mid + 1
    else:
        right = mid

print(right)
