from collections import deque
def solution(land):
    l = len(land)
    m = len(land[0])
    arr = [0 for i in range(m)]
    visited = [[False] * m for i in range(l)]
    for x in range(l):
        for y in range(m):
            if not visited[x][y] and land[x][y] == 1:
                BFS(land,arr,visited,x,y)
    print(arr)
    return max(arr)

def BFS(land,arr,visited,x,y):
    y_dir = set()
    y_dir.add(y)
    stack = deque([(x,y)])
    visited[x][y] = True
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    count=1
    while stack:
        x,y = stack.popleft()
        for i in directions:
            xs,ys = x+i[0],y+i[1]
            if 0<=xs<len(land) and 0<=ys<len(land[0]):
                if not visited[xs][ys] and land[xs][ys] == 1:
                    y_dir.add(ys)
                    visited[xs][ys] = True
                    stack.append([xs,ys])
                    count+=1
    for i in y_dir:
        arr[i] += count
