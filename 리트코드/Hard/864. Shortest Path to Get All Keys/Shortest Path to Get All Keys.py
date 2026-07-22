from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        g = []
        for x in grid:
            g.append(list(x))

        n = len(g)
        m = len(g[0])
        keys_cnt = 0
        keys_idx = {}
        for i in range(n):
            for j in range(m):
                if g[i][j] == "@":
                    start = [i,j]
                    g[i][j] = "."
                elif g[i][j].islower():
                    keys_idx[g[i][j]] = keys_cnt
                    keys_cnt += 1

        visited = [[[False] * (1 << keys_cnt) for _ in range(m)] for _ in range(n)]
        
        queue = deque([(start[0],start[1],1,0)])
        visited[start[0]][start[1]][0] = True
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        target = (1 << keys_cnt) - 1
        while queue:
            x,y,cnt,key = queue.popleft()
            for dx,dy in directions:
                sx,sy = x+dx,y+dy
                if 0<=sx<n and 0<=sy<m:
                    if  g[sx][sy] == "." and not visited[sx][sy][key]:
                        queue.append((sx,sy,cnt+1,key))
                        visited[sx][sy][key] = True
                    elif g[sx][sy].islower():
                        next_key = key | (1 << keys_idx[g[sx][sy]])
                        if next_key == target:
                            return cnt
                        
                        if not visited[sx][sy][next_key]:
                            queue.append((sx,sy,cnt+1,next_key))
                            visited[sx][sy][next_key] = True
                    elif g[sx][sy].isupper() and not visited[sx][sy][key]:
                        door_idx = keys_idx[g[sx][sy].lower()]
                        if key & (1 << door_idx):
                            queue.append((sx,sy,cnt+1,key))
                            visited[sx][sy][key] = True
        return -1