def solution(key, lock):
    n = 0
    l = len(lock)
    k = len(key)
    graph = [[0] * (3*l-2) for i in range((3*l-2))]
    
    for i in range(l):
        for j in range(l):
            graph[l - 1 + i][l - 1 + j] = lock[i][j]
            
    while True:
        if n == 4:
            break
            
        if check(graph,lock,key,l,k):
            return True
        key = rotate(key,k)
        n+=1

    return False

def check(graph,lock,key, l ,k):
    for n in range(3*l-1-k):
        for m in range(3*l-1-k):
            if check2(graph, key, k,n,m,l):
                return True
            
    return False
def check2(graph, key, k,n,m,l):
    modified = []
    modified1 = []
    for i in range(k):
        for j in range(k):
            if graph[n+i][m+j] == 0 and key[i][j] == 1:
                graph[n+i][m+j] = 1
                modified.append((n + i, m + j))
            elif graph[n+i][m+j] == 1 and key[i][j] == 1:
                graph[n + i][m + j] = 0
                modified1.append((n + i, m + j))
                break
    
    isbool = False
    if all(graph[l-1+i][l-1+j] == 1 for i in range(l) for j in range(l)):
        isbool = True
        
    for x, y in modified:
        graph[x][y] = 0
    for x,y in modified1:
        graph[x][y] = 1
        
    return isbool
    

def rotate(graph, n):
    graph1= [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            graph1[i][j] = graph[n-j-1][i]
    return graph1