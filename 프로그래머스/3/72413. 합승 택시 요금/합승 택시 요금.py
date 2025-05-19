def solution(n, s, a, b, fares):
    arr = floid(fares,n)
    index = [sum(x) for x in zip(arr[a-1], arr[b-1], arr[s-1])]
    return min(index)


def floid(graph, n):
    dist = [[float('inf')] * n for i in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for x,y,cost in graph:
        dist[x-1][y-1] = cost
        dist[y-1][x-1] = cost

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist    
