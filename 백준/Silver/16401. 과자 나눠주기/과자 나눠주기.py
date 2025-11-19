import sys

input = sys.stdin.readline

n,m = map(int, input().split())

arr = list(map(int, input().split()))
left =  0
right = max(arr) + 1

while left + 1 < right:
    mid = (left+right) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid

    if cnt >= n:
        left = mid
    else:
        right = mid

print(left)
