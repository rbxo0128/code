import sys

n= int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

result = [0] * (n+1)

for i in range(n-1,-1,-1):
    if i + graph[i][0] <= n:
        result[i] = max(graph[i][1] + result[i + graph[i][0]], result[i+1])
    else:
        result[i] = result[i+1]

print(result[0])