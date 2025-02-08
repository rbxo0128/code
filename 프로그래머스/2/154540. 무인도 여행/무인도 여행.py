def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y):
        stack = [(x, y)]
        visited[x][y] = True
        total_food = int(maps[x][y])

        while stack:
            cx, cy = stack.pop()
            
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    total_food += int(maps[nx][ny])
                    stack.append((nx, ny))

        return total_food
    
    result = []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                result.append(dfs(i, j))
    
    if not result:
        result.append(-1)
    
    result.sort()
    return result 
    