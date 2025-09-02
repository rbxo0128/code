def solution(targets):
    targets.sort(key = lambda x:x[1])
    count=1
    temp = targets[0][1]
    for x,y in targets:
        if temp <= x:
            count+=1
            temp = y
            
    return count