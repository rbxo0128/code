import sys
from collections import deque

input = sys.stdin.readline

board = []

directions = [(0,1),(-1,1),(1,0),(1,1)]

visited = [[[False] * 4 for i in range(19)] for i in range(19)]
def check(x,y,stone):
    for idx,(dx,dy) in enumerate(directions):
        cnt = 0
        visited[x][y][idx] = True
        for i in range(1,6):
            if 0<= x+i*dx < 19 and 0<= y+i*dy < 19: 
                if board[x+i*dx][y+i*dy] == stone and not visited[x+i*dx][y+i*dy][idx]:
                    cnt += 1
                    visited[x+i*dx][y+i*dy][idx] = True
                
                elif board[x+i*dx][y+i*dy] != stone:
                    break
                
        if cnt == 4:
            return True
        
    return False


for i in range(19):
    board.append(list(map(int, input().split())))

for i in range(19):
    for j in range(19):
        if board[j][i] in [1,2]:
            if check(j,i,board[j][i]):
                print(board[j][i])
                print(j+1,i+1)
                exit()

print(0)