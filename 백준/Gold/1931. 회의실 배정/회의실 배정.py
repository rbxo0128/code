N = int(input())
arr = []
for i in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort(key=lambda x: (x[1], x[0]))

count = 0
time = 0
for start, end in arr:
    if start >= time:
        count += 1
        time = end

print(count)