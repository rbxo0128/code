import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

left = 0
right = n-1

answer = float("inf")
l,r = 0,0
while left < right:
    total = arr[left] + arr[right]

    if answer > abs(total):
        answer = abs(total)
        l,r = left, right

    if total < 0:
        left+=1
    elif total > 0:
        right-=1
    elif total == 0:
        break

print(arr[l], arr[r])