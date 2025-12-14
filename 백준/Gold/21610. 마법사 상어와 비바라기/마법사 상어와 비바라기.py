import sys
from collections import deque

input = sys.stdin.readline

#dir 0,1,2,3,4,5,6,7
dirx = [0, -1, -1, -1, 0, 1, 1, 1]
diry = [-1, -1, 0, 1, 1, 1, 0, -1]

n,m= map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

ops = []
for i in range(m):
    ops.append(list(map(int, input().split())))

cloud = []
cloud.append((n-1,0))
cloud.append((n-1,1))
cloud.append((n-2,0))
cloud.append((n-2,1))

def move(op, cloud):
    d,s = op
    dx,dy = dirx[d-1] * s, diry[d-1] * s

    new_cloud = []
    for x,y in cloud:
        new_cloud.append(((x+dx)%n, (y+dy) %n))

    return new_cloud

directions = [(-1,-1),(-1,1),(1,1),(1,-1)]
def pluswater(cloud, cloud_set):
    for x,y in cloud:
        board[x][y] += 1

        for dx,dy in directions:
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<n and (board[sx][sy] or (sx,sy) in cloud_set):
                board[x][y] += 1

def newcloud(cloud, cloud_set):
    new_cloud = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2:
                if (i,j) in cloud_set:
                    continue
                board[i][j] -= 2
                new_cloud.append((i,j))

    return new_cloud

for i in range(m):
    cloud = move(ops[i], cloud)
    cloud_set = set(cloud)
    pluswater(cloud,cloud_set)
    cloud = newcloud(cloud, cloud_set)

answer = 0
for i in range(n):
    answer += sum(board[i])
print(answer)