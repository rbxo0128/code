import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

board = [[False] * 5 for i in range(5)]
board_dict = {}
for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        board_dict[arr[j]] = (i,j)

def check():
    cnt = 0
    for i in range(5):
        if all(board[i][j] for j in range(5)):
            cnt += 1
    
    for j in range(5):
        if all(board[i][j] for i in range(5)):
            cnt += 1
    
    if all(board[i][i] for i in range(5)):
        cnt += 1

    if all(board[i][4 - i] for i in range(5)):
        cnt += 1
    
    if cnt >= 3:
        return True

    return False


for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        x,y = board_dict[arr[j]]
        board[x][y] = True
        if check():
            print(i*5 + j + 1)
            exit()