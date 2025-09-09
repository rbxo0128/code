import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

apples = set()
for i in range(k):
    x,y = map(int, input().split())
    apples.add((x,y))

l = int(input())

ops = {}
move_dict = {"L": -1,"D": 1}
for i in range(l):
    time,op = input().split()
    ops[int(time)] = move_dict[op]

stack = deque()
stack.append((1,1))

#RLUD
directions = [(0,1), (1,0),(0,-1),(-1,0)]

direct = 0
time = 0
while True:
    x,y = stack[-1]
    dx,dy = directions[direct]
    sx,sy = x+dx, y+dy
    time += 1
    if time in ops:
        direct = (direct+ops[time])%4

    if 0<sx<=n and 0<sy<=n:
        if (sx,sy) in stack:
            print(time)
            break

        if (sx,sy) not in apples:
            stack.popleft()
        else:
            apples.remove((sx,sy))

        stack.append((sx,sy))
    else:
        print(time)
        break
