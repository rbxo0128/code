import sys

n = int(sys.stdin.readline())

arr = {}
for i in range(n):
    title = sys.stdin.readline().strip()
    if title in arr:
        arr[title] += 1
    else:
        arr[title] = 1

arr = sorted(arr.items(), key=lambda x: (-x[1], x[0]))

print(arr[0][0])