import sys
input = sys.stdin.readline

n= int(input())

arr = []
for i in range(n):
    year,y = input().split()
    start = int(year[0:4])*12 + int(year[5:])
    end = int(y[0:4])*12 + int(y[5:])
    arr.append((start,end))

years = []
for l, r in arr:
    years.append((l, 1))
    years.append((r + 1, -1))

years.sort()

cnt = 0
max_cnt = 0
answer = 0

for year, check in years:
    cnt += check
    if cnt > max_cnt:
        max_cnt = cnt
        answer = year

if answer%12 == 0:
    print(str(answer//12-1) + "-12")
else:
    print(str(answer//12) + "-" + str(answer%12).zfill(2))