import sys
from collections import deque

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr2 = deque()

for i in range(len(arr)):
    arr2.append((arr[i], i))


while arr2:
    num, idx = arr2.popleft()
    print(idx+1)

    if num < 0:
        for i in range(-num):
            if arr2:
                x = arr2.pop()
                arr2.appendleft(x)

    else:
        for i in range(num-1):
            if arr2:
                x = arr2.popleft()
                arr2.append(x)