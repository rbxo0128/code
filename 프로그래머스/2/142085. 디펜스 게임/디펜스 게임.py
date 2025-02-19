import heapq

def solution(n, k, enemy):
    
    heap = []
    enemySum = 0
    result = 0
    for i in enemy:
        result+=1
        heapq.heappush(heap, -i)
        enemySum += i
        
        if(enemySum > n):
            if k==0:
                return result-1
            else:
                m = heapq.heappop(heap)
                enemySum += m
                k -= 1

    return result