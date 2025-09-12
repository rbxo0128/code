import sys
import math
from collections import deque

input = sys.stdin.readline

l, e, w, s, n = map(int, input().split())

e = e/100
w = w/100
s = s/100
n = n/100

visited = [[False]*30 for i in range(30)]
x, y = 15, 15
visited[x][y] = True

def DFS(level,prob,visited,x,y):
    if level == l:
        return prob

    result = 0
    for i in range(4):
        nx,ny = 0,0
        if i == 0:
            ny+=1
            p = e
        elif i == 1:
            ny-=1
            p = w
        elif i == 2:
            nx+=1
            p=s
        elif i == 3:
            nx-=1
            p=n

        if visited[x+nx][y+ny]:
            continue
        
        else:
            visited[x+nx][y+ny] = True
            result += DFS(level+1,prob*p,visited,x+nx,y+ny)
            visited[x+nx][y+ny] = False

    return result

answer = 0
for i in range(4):
    nx,ny = 0,0
    if i == 0:
        ny+=1
        p = e
    elif i == 1:
        ny-=1
        p = w
    elif i == 2:
        nx+=1
        p=s
    elif i == 3:
        nx-=1
        p=n

    visited[x+nx][y+ny] = True
    answer += DFS(1,p,visited,x+nx,y+ny)
    visited[x+nx][y+ny] = False

print(answer)