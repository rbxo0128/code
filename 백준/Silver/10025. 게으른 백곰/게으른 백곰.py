import sys

n,m = map(int,sys.stdin.readline().split())

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
arr.sort(key= lambda x : x[1])

tmp = 0
left=0
right=0
cnt=0

while right < n:
    while arr[right][1] <= arr[left][1]+2*m:
        cnt += arr[right][0]
        right += 1

        if right >= n:
            break

    tmp = max(tmp, cnt)

    cnt -= arr[left][0]
    left += 1

print(tmp)
