max_sheep = 1
def solution(info, edges):
    tree = {}
    for x,y in edges:
        if x in tree:
            tree[x].append(y)
        else:
            tree[x] = [y]
        
        if y in tree:
            tree[y].append(x)
        else:
            tree[y] = [x]
    visited = [False for i in range(len(info))]
    stack = set()
    stack.add(0)
    visited[0] = True
    sheepwolf = {0:1, 1:0}
    answer = 0
    
    def DFS(start, visited, stack, sheepwolf):
        global max_sheep
        for j in stack:
            for i in tree[j]:
                if not visited[i]:
                    if info[i] == 0:
                        sheepwolf[0] += 1
                        max_sheep = max(max_sheep, sheepwolf[0])
                        visited[i] = True
                        stack.add(i)
                        DFS(i, visited, stack, sheepwolf)
                        stack.remove(i)
                        visited[i] = False
                        sheepwolf[0] -= 1
                    else:
                        if sheepwolf[0] - 1 == sheepwolf[1]:
                            continue
                        else:
                            sheepwolf[1] += 1
                            visited[i] = True
                            stack.add(i)
                            DFS(i, visited, stack, sheepwolf)
                            stack.remove(i)
                            visited[i] = False
                            sheepwolf[1] -= 1

    DFS(0, visited, stack, sheepwolf)
    
    return max_sheep

    