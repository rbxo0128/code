import sys
input = sys.stdin.readline

n = int(input())
trains = [tuple(map(int, input().split())) for i in range(n)]

x, y = trains[n-1]
cnt = 1
tmp = y

for i in range(n - 2, -1, -1):
    start, end = trains[i]
    
    if start > tmp:
        cnt += 1
        tmp = end
    else:
        tmp = min(end, tmp) 

print(cnt)