import sys
from collections import deque

input = sys.stdin.readline

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs():
    shapes = set()
    q = deque()
    q.append([(0,0)])
    
    while q:
        shape = q.popleft()
        if len(shape) == 4:
            min_x = min(x for x, _ in shape)
            min_y = min(y for _, y in shape)
            temp = tuple(sorted((x-min_x, y-min_y) for x,y in shape))
            shapes.add(temp)
            continue

        for x, y in shape:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in shape:
                    q.append(shape + [(nx, ny)])
    return list(shapes)


n,m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

shapes = dfs()

answer = 0
for i in range(n):
    for j in range(m):
        for shape in shapes:
            total = 0
            can_shape = True
            for dx, dy in shape:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    total += board[x][y]
                else:
                    can_shape = False
                    break
            if can_shape and total > answer:
                answer = total
print(answer)