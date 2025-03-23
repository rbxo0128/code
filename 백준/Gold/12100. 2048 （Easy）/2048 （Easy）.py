import heapq
import sys

def DFS(graph, cnt, answer):
    if cnt == 5:
        maxnum = max(max(i) for i in graph)
        answer.append(maxnum)
        return
    
    n = len(graph)
    check = [i[:] for i in graph]
    #LRUD
    # 일단 0 은 무시하고 와야되고 같은게 있으면 합쳐지면서 움직여야된다
    #L
    graph2 = [[0]*n for i in range(n)]
    for i in range(n):
        prev = -1
        result = []
        for j in range(n):
            if graph[i][j] == 0:
                continue

            if prev == graph[i][j]:
                result[-1] = 2*prev
                prev = -1

            else:
                result.append(graph[i][j])
                prev = graph[i][j]
        
        for j in range(len(result)):
            graph2[i][j] = result[j]

    if not check == graph2:
        DFS(graph2,cnt+1,answer)

    #R
    graph2 = [[0]*n for i in range(n)]
    for i in range(n):
        prev = -1
        result = []
        for j in range(n-1,-1,-1):
            if graph[i][j] == 0:
                continue

            if prev == graph[i][j]:
                result[-1] = 2*prev
                prev = -1

            else:
                result.append(graph[i][j])
                prev = graph[i][j]
        
        for j in range(len(result)):
            graph2[i][n-1-j] = result[j]

    if not check == graph2:
        DFS(graph2,cnt+1,answer)

    #U
    graph2 = [[0]*n for i in range(n)]
    for i in range(n):
        prev = -1
        result = []
        for j in range(n):
            if graph[j][i] == 0:
                continue

            if prev == graph[j][i]:
                result[-1] = 2*prev
                prev = -1

            else:
                result.append(graph[j][i])
                prev = graph[j][i]
        
        for j in range(len(result)):
            graph2[j][i] = result[j]

    if not check == graph2:
        DFS(graph2,cnt+1,answer)

    #D
    graph2 = [[0]*n for i in range(n)]
    for i in range(n):
        prev = -1
        result = []
        for j in range(n-1,-1,-1):
            if graph[j][i] == 0:
                continue

            if prev == graph[j][i]:
                result[-1] = 2*prev
                prev = -1

            else:
                result.append(graph[j][i])
                prev = graph[j][i]
        
        for j in range(len(result)):
            graph2[n-1-j][i] = result[j]

    if not check == graph2:
        DFS(graph2,cnt+1,answer)


n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

if n == 1:
    print(graph[0][0])

else:
    answer = []
    DFS(graph,0,answer)
    print(max(answer))