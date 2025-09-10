def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left=1
    right=distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        length = 0
        cnt = 0
        
        for rock in rocks:
            if rock - length < mid:
                cnt += 1
            else:
                length = rock
        
        if cnt > n:  
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
            
    return answer
