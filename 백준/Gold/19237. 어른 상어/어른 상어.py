import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[0 for i in range(n)] for i in range(n)]
queue = []

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j]:
            graph[i][j] = (arr[j],k)
            queue.append((arr[j],i,j))

sharks_dir = [x - 1 for x in map(int, input().split())]
#위 아래 왼쪽 오른쪽
directions = [(-1,0),(1,0),(0,-1),(0,1)]

sharks = []
for i in range(m):
    shark = []
    for j in range(4):
        shark.append([x - 1 for x in map(int, input().split())])

    sharks.append(shark)

answer = 0

def BFS(queue):
    new_queue = deque()
    while queue:
        num, x, y = queue.popleft()
        s_dir = sharks_dir[num-1]

        my_place = False
        can_move = False

        for i in sharks[num-1][s_dir]:
            dx,dy = directions[i]
            sx,sy = x+dx,y+dy
            if 0<=sx<n and 0<=sy<n:
                if graph[sx][sy] == 0:
                    new_queue.append((num,sx,sy))
                    sharks_dir[num-1] = i
                    can_move = True
                    break

                else:
                    if graph[sx][sy][0] == num and not my_place:
                        my_place = [i,sx,sy]

        if not can_move:
            idx,x,y = my_place
            sharks_dir[num-1] = idx
            new_queue.append((num,x,y))
    
    new_queue2 = deque()
    for num,x,y in new_queue:
        if graph[x][y] == 0 or graph[x][y][0] == num:
            graph[x][y] = (num,k)
            new_queue2.append((num,x,y))

    return new_queue2

def loss():
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                graph[i][j] = (graph[i][j][0], graph[i][j][1]-1)

def check():
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and graph[i][j][1] == 0:
                graph[i][j] = 0

queue.sort()
queue = deque(queue)

while True:
    answer += 1
    loss()
    queue = BFS(queue)
    check()
    if len(queue) == 1:
        print(answer)
        exit()

    if answer >= 1000:
        print(-1)
        exit()
