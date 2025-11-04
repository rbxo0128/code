from itertools import permutations

def solution(k, dungeons):
    l = len(dungeons)
    result = []
    arr = [i for i in range(l)]
    
    seq = permutations(arr,l)
    
    for j in seq:
        health = k
        count=0
        for i in j:
            if health >= dungeons[i][0]:
                health -= dungeons[i][1]
                count+=1
        
        result.append(count)
        
    print(result)
    answer = -1
    return max(result)