import sys

n, m, inven = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

maxs = max(max(i) for i in graph)

block = [0]*(maxs+1)  

for i in graph:
    for j in i:
        block[j] += 1

tmp = float("inf")
tmp2 = 0

for wall in range(maxs+1):
    count = 0
    count2 = 0

    for i in range(wall + 1, maxs+1):
        count += (i - wall) * block[i]

    for i in range(0, wall):
        count2 += (wall - i) * block[i]

    if count + inven >= count2:
        time = count * 2 + count2

        if time < tmp or (time == tmp and wall > tmp2):
            tmp = time
            tmp2 = wall

print(tmp, tmp2)