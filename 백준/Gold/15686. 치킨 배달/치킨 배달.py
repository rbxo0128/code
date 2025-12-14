import sys
from collections import deque
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i,j])
        elif graph[i][j] == 2:
            chicken.append([i,j])

arr = combinations(chicken,m)

result = []

for i in arr:
    sum1 = 0
    for x,y in house:
        mi = float("inf")
        for dx,dy in i:
            temp = abs(x-dx)+abs(y-dy)
            if temp < mi:
                mi = temp
        sum1+=mi

    result.append(sum1)

print(min(result))