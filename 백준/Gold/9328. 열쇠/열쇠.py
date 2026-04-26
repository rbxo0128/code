import sys
from collections import deque, defaultdict

input = sys.stdin.readline

t = int(input())

directions = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(t):
    n, m = map(int, input().split())
    
    graph_input = [list(input().strip()) for _ in range(n)]
    
    key_input = input().strip()
    keys = set() if key_input == '0' else set(key_input)

    graph = [['.'] * (m+2)]
    for row in graph_input:
        graph.append(['.'] + row + ['.'])
    graph.append(['.'] * (m+2))

    n += 2
    m += 2

    doors = defaultdict(list)
    
    def BFS():
        visited = [[False]*m for _ in range(n)]
        queue = deque([(0,0)])
        visited[0][0] = True
        
        answer = 0

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                sx, sy = x + dx, y + dy

                if 0<= sx < n and 0<= sy < m and not visited[sx][sy]:
                    if graph[sx][sy] == '*':
                        continue

                    if 'A' <= graph[sx][sy] <= 'Z':
                        if graph[sx][sy].lower() not in keys:
                            doors[graph[sx][sy]].append((sx, sy))
                            continue

                    visited[sx][sy] = True

                    if graph[sx][sy] == '$':
                        answer += 1
                        graph[sx][sy] = '.'

                    elif 'a' <= graph[sx][sy] <= 'z':
                        if graph[sx][sy] not in keys:
                            keys.add(graph[sx][sy])

                            if graph[sx][sy].upper() in doors:
                                for dx, dy in doors[graph[sx][sy].upper()]:
                                    queue.append((dx, dy))
                                del doors[graph[sx][sy].upper()]

                    queue.append((sx, sy))

        return answer

    print(BFS())