import sys
from collections import deque
input = sys.stdin.readline

n = input().strip()

total = int(n[0:2]) * 60 + int(n[3:])
total //= 10

visited =[False] * 367
visited2 = [False] * 367

queue = deque()
queue.append((0,0,False))
visited[0] = True

def BFS():
    while queue:
        x,cnt,start = queue.popleft()
        if x == total and start:
            print(cnt)
            exit()

        if x + 1 <= total:
            if start and not visited2[x+1]:
                visited2[x+1] = True
                queue.append((x+1,cnt+1,start))

            elif not start and not visited[x+1]:
                visited[x+1] = True
                queue.append((x+1, cnt+1, start))

        if x + 6 <= total:
            if start and not visited2[x+6]:
                visited2[x+6] = True
                queue.append((x+6,cnt+1,start))

            elif not start and not visited[x+6]:
                visited[x+6] = True
                queue.append((x+6, cnt+1, start))

        if x + 60 <= total:
            if start and not visited2[x+60]:
                visited2[x+60] = True
                queue.append((x+60,cnt+1,start))

            elif not start and not visited[x+60]:
                visited[x+60] = True
                queue.append((x+60, cnt+1, start))

        if start and x + 3 <= total:
            if not visited2[x+3]:
                visited2[x+3] = True
                queue.append((x+3,cnt+1,start))

        if not start:
            if x == 0:
                visited2[x+3] = True
                queue.append((x+3,cnt+1,True))

            elif not visited2[x]:
                visited2[x] = True
                queue.append((x,cnt+1, True))
BFS()