import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr_dict = {}
stack = []
answer = []
for i in arr:
    if i in arr_dict:
        arr_dict[i] += 1
    else:
        arr_dict[i] = 1

result = [-1] * n 
for i in range(n):
    while stack:
        if arr_dict[arr[i]] > arr_dict[arr[stack[-1]]]:
            result[stack.pop()] = arr[i]
        else:
            break
    stack.append(i)

print(" ".join(map(str, result)))