import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

board = [[0] * 52 for i in range(52)]
line = [[0] * 52 for i in range(52)]

def mapping(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    return ord(c) - ord('a') + 26

def BFS(start, end, parent):
    visited = [False] * 52
    q = deque([start])
    visited[start] = True

    while q:
        x = q.popleft()
        for i in range(52):
            if not visited[i] and board[x][i] - line[x][i] > 0:
                parent[i] = x
                visited[i] = True
                if i == end:
                    return True
                q.append(i)
    return False

for i in range(n):
    x, y, w = input().split()
    u = mapping(x)
    v = mapping(y) 
    w = int(w)

    board[u][v] += w
    board[v][u] += w

answer = 0
parent = [-1]*52

start = mapping("A")
end = mapping("Z")

while BFS(start, end, parent):
    a = float('inf')
    v = end
    while v != start:
        u = parent[v]
        a = min(a, board[u][v] - line[u][v])
        v = u

    v = end
    while v != start:
        u = parent[v]
        line[u][v] += a
        line[v][u] -= a
        v = u

    answer += a

print(answer)