import sys
import copy

n, m = map(int, sys.stdin.readline().split())
graph = []
cctvs = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
    for j in range(m):
        if 1 <= row[j] <= 5:
            cctvs.append((row[j], i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mode = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
    5: [[0, 1, 2, 3]]
}

min_count = n * m

def detect(board, x, y, direction):
    nx, ny = x, y
    while True:
        nx += dx[direction]
        ny += dy[direction]
        if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] == 6:
            break
        if board[nx][ny] == 0:
            board[nx][ny] = '#'

def DFS(cctv_idx, graph):
    global min_count

    if cctv_idx == len(cctvs):
        count = 0
        for i in range(n):
            count += graph[i].count(0)
        min_count = min(min_count, count)
        return

    cctv_type, x, y = cctvs[cctv_idx]
    
    for directions in mode[cctv_type]:
        board_copy = copy.deepcopy(graph)
        
        for d in directions:
            detect(board_copy, x, y, d)
            
        DFS(cctv_idx + 1, board_copy)
        

DFS(0, graph)

print(min_count)