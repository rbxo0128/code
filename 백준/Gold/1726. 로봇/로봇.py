import sys
from collections import deque

input = sys.stdin.readline

#dir 0,1,2,3 동 서 남 북
directions = [(0,1),(0,-1),(1,0),(-1,0)]

def BFS():
    queue = deque()
    queue.append((start_x-1,start_y-1,start_dir-1))
    visited = [[[False] * 4 for i in range(m)] for i in range(n)]
    visited[start_x-1][start_y-1][start_dir-1] = True
    cnt = 0
    while queue:
        for i in range(len(queue)):
            x,y,dir = queue.popleft()

            if x == end_x-1 and y == end_y-1 and dir == end_dir-1:
                return cnt
            
            dx,dy = directions[dir]
            for idx in range(1,4):
                sx,sy = x+dx*idx,y+dy*idx
                if 0<=sx<n and 0<=sy<m and board[sx][sy] == 0:
                    if not visited[sx][sy][dir]:
                        queue.append((sx,sy,dir))
                        visited[sx][sy][dir] = True

                else:
                    break

            right_turn = {0:2, 2:1, 1:3, 3:0}
            left_turn  = {0:3, 3:1, 1:2, 2:0}

            r = right_turn[dir]
            if not visited[x][y][r]:
                queue.append((x, y, r))
                visited[x][y][r] = True

            l = left_turn[dir]
            if not visited[x][y][l]:
                queue.append((x, y, l))
                visited[x][y][l] = True

        cnt += 1

    return -1

n,m= map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

start_x,start_y,start_dir = map(int, input().split())
end_x,end_y,end_dir = map(int, input().split())

print(BFS())