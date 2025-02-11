from collections import deque
def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    
    for i in range(n):
        storage[i] = '0'+storage[i]+'0'
    
    a = ['0'*(m+2)]
    storage = a+storage+a

    for i in requests:
        if len(i) == 2:
            pickup(n+2,m+2,i[0],storage)
        else:
            BFS(n+2,m+2,i,storage)
    
    count = 0
    for i in range(n+2):
        for j in range(m+2):
            if storage[i][j] == "0":
                count+=1
    answer = (n+2)*(m+2) - count
    
    return answer

def BFS(n,m, letter, storage):
    visited = [[False]*m for i in range(n)]
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    visited[0][0] = True
    stack = deque()
    stack.append((0,0))
    
    while stack:
        x,y = stack.popleft()
        for dx,dy in direction:
            sx,sy = x+dx, y+dy
            if 0<=sx<n and 0<=sy<m and not visited[sx][sy]:
                if storage[sx][sy] == "0":
                    visited[sx][sy] = True
                    stack.append((sx,sy))
                    
                elif storage[sx][sy] == letter:
                    visited[sx][sy] = True
                    storage[sx] = storage[sx][0:sy]+"0"+storage[sx][sy+1:]
                    
def pickup(n,m,letter,storage):
    for i in range(n):
        for j in range(m): 
            if storage[i][j] == letter:
                storage[i] = storage[i][0:j]+"0"+storage[i][j+1:]