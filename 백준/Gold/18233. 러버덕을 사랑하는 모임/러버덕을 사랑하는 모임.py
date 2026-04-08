import sys
from itertools import combinations

input = sys.stdin.readline

n, p, e = map(int, input().split())

idx = [i for i in range(n)]
members = []
for i in range(n):
    members.append(list(map(int, input().split())))

for nums in combinations(idx,p):
    sumx = 0
    sumy = 0

    for i in nums:
        sumx += members[i][0]
        sumy += members[i][1]

    if sumx <= e <= sumy:
        answer = [0] * n

        for i in nums:
            answer[i] = members[i][0]

        x = e - sumx

        for i in nums:
            rest = members[i][1] - members[i][0]
            add = min(x, rest)
            answer[i] += add
            x -= add

        print(" ".join(map(str, answer)))
        break

else:
    print(-1)