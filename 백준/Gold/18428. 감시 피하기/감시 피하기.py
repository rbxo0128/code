import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

board = []
for i in range(n):
    board.append(list(input().split()))

teachers = []
for i in range(n):
    for j in range(n):
        if board[i][j] == "T":
            teachers.append((i,j))

directions = [(0,1),(0,-1),(1,0),(-1,0)]
def get_can_blocks():
    blocks = set()
    for x,y in teachers:
        for dx,dy in directions:
            new_blocks = set()
            sx,sy = x,y
            while True:
                sx,sy = sx+dx,sy+dy
                if 0<=sx<n and 0<=sy<n:
                    if board[sx][sy] == "X":
                        new_blocks.add((sx,sy))

                    elif board[sx][sy] == "S":
                        blocks = blocks.union(new_blocks)
                        break

                    elif board[sx][sy] == "O":
                        break

                else:
                    break
    
    return list(blocks)

def check(*blocks):
    blocks = set(blocks)
    for x,y in teachers:
        for dx,dy in directions:
            sx,sy = x,y
            while True:
                sx,sy = sx+dx,sy+dy
                if 0<=sx<n and 0<=sy<n:
                    if board[sx][sy] == "S":
                        return False
                    elif (sx,sy) in blocks or board[sx][sy] == "O":
                        break
                    
                else:
                    break
    return True                     

can_blocks = get_can_blocks()

l = min(3,len(can_blocks))

for a in combinations(can_blocks, l):
    if check(*a):
        print("YES")
        break

else:
    print("NO")