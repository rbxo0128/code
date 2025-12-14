import sys

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

total = sum(sum(i) for i in graph)

result = []

def calc(cur):
    cur_score = 0
    for x in range(len(cur)):
        for y in range(x + 1, len(cur)):
            cur_score += graph[cur[x]][cur[y]]
            cur_score += graph[cur[y]][cur[x]]
    return cur_score

def DFS(cur, start):
    if len(cur) == n // 2:
        team2 = [i for i in range(n) if i not in cur]
        cur_score = calc(cur)
        score2 = calc(team2)
        result.append(abs(cur_score - score2))
        return

    for i in range(start, n):
        cur.append(i)
        DFS(cur, i + 1)
        cur.pop()

DFS([], 0)

print(min(result))
