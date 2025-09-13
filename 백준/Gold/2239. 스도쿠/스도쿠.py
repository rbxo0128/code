import sys

input = sys.stdin.readline

width = [[False] * 9 for i in range(9)]
height = [[False] * 9 for i in range(9)]
square = [[False] * 9 for i in range(9)]

board = []
for i in range(9):
    board.append(list(map(int,input().strip())))

add_list = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            add_list.append((i,j))

        else:
            width[i][board[i][j]-1] = True
            square[(i//3)*3 + (j//3)][board[i][j]-1] = True
            height[j][board[i][j]-1] = True

def DFS(level,result, width, height, square):
    if level == len(add_list):
        return True
    
    x,y = add_list[level]
    for j in range(9):
        if not width[x][j] and not height[y][j] and not square[(x//3)*3 + (y//3)][j]:
            width[x][j] =  True
            height[y][j] = True
            square[(x//3)*3 + (y//3)][j] = True
            result.append((x,y,j+1))
            if DFS(level+1,result, width, height, square):
                return True
            result.pop()
            width[x][j] =  False
            height[y][j] = False
            square[(x//3)*3 + (y//3)][j] = False

    return False

result = []
DFS(0, result, width, height, square)

for x,y,z in result:
    board[x][y] = z

for nums in board:
    print(''.join(map(str,nums)))