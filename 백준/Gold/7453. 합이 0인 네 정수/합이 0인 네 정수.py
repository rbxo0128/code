import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
    
n = int(input())

arr = [[] for i in range(4)]

for i in range(n):
    a, b, c, d = map(int, input().split())
    arr[0].append(a)
    arr[1].append(b)
    arr[2].append(c)
    arr[3].append(d)

ab = []
cd = []

for i in range(n):
    for j in range(n):
        ab.append(arr[0][i]+arr[1][j])
        cd.append(arr[2][i]+arr[3][j])

ab.sort()
cd.sort()

left = 0
right = len(cd) - 1

cnt = 0
while left< len(ab) and right >= 0:
    total = ab[left] + cd[right]
    
    if total < 0:
        left += 1
    elif total > 0:
        right -= 1
    elif total == 0:
        a = ab[left]
        b = cd[right]
        a_cnt = 0
        b_cnt = 0
        while left < len(ab) and a == ab[left]:
            left+=1
            a_cnt+=1

        while right >= 0 and b == cd[right]:
            right-=1
            b_cnt+=1

        cnt += a_cnt*b_cnt

print(cnt)