import sys

n,m = map(int, sys.stdin.readline().split())

graph = [list(map(int, input().strip())) for i in range(n)]

max_rect = min(n,m)

for num in range(max_rect+1,0,-1):
    for i in range(n-num+1):
        for j in range(m-num+1):
            if graph[i][j] == graph[i][j+num-1] == graph[i+num-1][j] == graph[i+num-1][j+num-1]:
                print(num*num)
                exit()