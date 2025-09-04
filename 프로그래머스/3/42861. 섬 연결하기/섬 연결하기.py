def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    
    check = set()
    answer = 0
    parents = {}
    
    def find(x):
        if x not in parents:
            parents[x] = x
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
        
        
    def union(a,b):
        a = find(a)
        b = find(b)
        
        if a != b:
            parents[a] = b

    for x,y,cost in costs:
        if not find(x) == find(y):
            answer += cost
            union(x,y)
            
    return answer