import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n,m= map(int,input().split())

    graph = []

    for i in range(n):
        graph.append(list(input().strip()))

    keys = set(input().strip())

    queue = deque()
    doors = {}
    answer = 0

    for i in range(n):
        if graph[i][0] == ".":
            queue.append((i,0))

        elif "a"<=graph[i][0]<="z":
            queue.append((i,0))
            keys.add(graph[i][0])
        
        elif "A"<=graph[i][0]<="Z":
            if graph[i][0] in doors:
                doors[graph[i][0]].append((i,0))
            else:
                doors[graph[i][0]] = [(i,0)]

        elif graph[i][0] == "$":
            answer += 1
            queue.append((i,0))

        if graph[i][m-1] == ".":
            queue.append((i,m-1))

        elif "a"<=graph[i][m-1]<="z":
            queue.append((i,m-1))
            keys.add(graph[i][m-1])

        elif "A"<=graph[i][m-1]<="Z":
            if graph[i][m-1] in doors:
                doors[graph[i][m-1]].append((i,m-1))
            else:
                doors[graph[i][m-1]] = [(i,m-1)]

        elif graph[i][m-1] == "$":
            answer+=1
            queue.append((i,m-1))
        
    for i in range(1,m-1):
        if graph[0][i] == ".":
            queue.append((0,i))

        elif "a"<=graph[0][i]<="z":
            queue.append((0,i))
            keys.add(graph[0][i])

        elif "A"<=graph[0][i]<="Z":
            if graph[0][i] in doors:
                doors[graph[0][i]].append((0,i))
            else:
                doors[graph[0][i]] = [(0,i)]

        elif graph[0][i] == "$":
            answer+=1
            queue.append((0,i)) 

        if graph[n-1][i] == ".":
            queue.append((n-1,i))

        elif "a"<=graph[n-1][i]<="z":
            queue.append((n-1,i))
            keys.add(graph[n-1][i])

        elif "A"<=graph[n-1][i]<="Z":
            if graph[n-1][i] in doors:
                doors[graph[n-1][i]].append((n-1,i))
            else:
                doors[graph[n-1][i]] = [(n-1,i)]

        elif graph[n-1][i] == "$":
            answer+=1
            queue.append((n-1,i))

    for key in keys:
        if key.upper() in doors:
            for x,y in doors[key.upper()]:
                queue.append((x,y))

    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    def BFS(queue,answer):
        visited = [[False]*m for i in range(n)]
        for x,y in queue:
            visited[x][y] = True

        while queue:
            x,y = queue.popleft()
            for dx,dy in directions:
                sx,sy = x+dx, y+dy
                if 0<= sx < n and 0<= sy < m and not visited[sx][sy]:
                    if graph[sx][sy] == "*":
                        continue

                    if graph[sx][sy] == "$":
                        visited[sx][sy] = True
                        queue.append((sx,sy))
                        answer += 1

                    elif graph[sx][sy] == ".":
                        visited[sx][sy] = True
                        queue.append((sx,sy))
                    
                    elif "A"<= graph[sx][sy] <= "Z":
                        if graph[sx][sy].lower() in keys:
                            visited[sx][sy] = True
                            queue.append((sx,sy))
                    
                        else:
                            if graph[sx][sy] in doors:
                                doors[graph[sx][sy]].append((sx,sy))
                            else:
                                doors[graph[sx][sy]] = [(sx,sy)]

                    elif "a" <= graph[sx][sy] <= "z":
                        keys.add(graph[sx][sy])
                        queue.append((sx,sy))
                        visited[sx][sy] = True
                        if graph[sx][sy].upper() in doors:
                            for x,y in doors[graph[sx][sy].upper()]:
                                visited[x][y] = True
                                queue.append((x,y))

                            del doors[graph[sx][sy].upper()]


        return answer

    print(BFS(queue,answer))