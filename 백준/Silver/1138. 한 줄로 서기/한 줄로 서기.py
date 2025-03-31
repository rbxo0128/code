import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

result = [-1 for i in range(n)]
for i in range(n):
    count = 0
    for j in range(n):
        if result[j] != -1:
            continue
        
        if count == arr[i]:
            result[j] = i+1
            break

        count += 1

print(' '.join(map(str,result)))