import sys
from collections import deque

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = deque()

for i in range(n-1,-1,-1):
    while stack:
        if stack[-1] <= arr[i]:
            stack.pop()
        else:
            break
    if stack:
        answer[i] = stack[-1]
        
    stack.append(arr[i])

print(' '.join(map(str,answer)))