import sys
from collections import deque

def BFS(start, dest):
    visited = set()
    queue = deque()
    queue.append((start, ''))
    visited.add(start)

    while queue:
        x, count = queue.popleft()

        if x == dest:
            return count

        d = (x * 2) % 10000
        if d not in visited:
            visited.add(d)
            queue.append((d, count + 'D'))

        s = 9999 if x == 0 else x - 1
        if s not in visited:
            visited.add(s)
            queue.append((s, count + 'S'))

        num_str = str(x).zfill(4)
        left = int(num_str[1:] + num_str[0])
        if left not in visited:
            visited.add(left)
            queue.append((left, count + 'L'))

        right = int(num_str[-1] + num_str[:-1])
        if right not in visited:
            visited.add(right)
            queue.append((right, count + 'R'))

n = int(sys.stdin.readline())

for i in range(n):
    start, dest = map(int, sys.stdin.readline().split())
    print(BFS(start, dest))
