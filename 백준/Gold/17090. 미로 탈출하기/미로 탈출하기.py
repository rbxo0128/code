from collections import deque
import sys
sys.setrecursionlimit(300000)

input = sys.stdin.readline

n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(input().strip()))

mem = [[0] * m for i in range(n)]

directions = {
    "U" : (-1,0),
    "R" : (0,1),
    "D" : (1,0),
    "L" : (0,-1)
}
back = set()
def DFS(x,y):
    if mem[x][y] in (1,-1):
        return mem[x][y]

    if mem[x][y] == 2:
        return -1

    mem[x][y] = 2

    dx,dy = directions[arr[x][y]]
    nx,ny = x+dx,y+dy

    if not (0 <= nx < n and 0 <= ny < m):
        mem[x][y] = 1
        return 1

    result = DFS(nx,ny)
    mem[x][y] = result
    return result

answer = 0
for i in range(n):
    for j in range(m):
        if mem[i][j] == 0:
            DFS(i,j)

answer = 0
for i in range(n):
    for j in range(m):
        if mem[i][j] == 1:
            answer += 1
print(answer)