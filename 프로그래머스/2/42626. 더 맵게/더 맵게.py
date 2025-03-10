import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while True:
        x = heapq.heappop(scoville)
        if x >= K:
            break
            
        if not scoville and x<K:
            return -1
            
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x+y*2)
        count+=1
    
    return count