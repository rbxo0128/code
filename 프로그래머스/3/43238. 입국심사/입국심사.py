def solution(n, times):
    left = 0
    right = n*max(times)
    
    answer = 0
    while left<=right:
        cnt = 0
        mid = (left+right)//2
        for i in times:
            cnt += mid//i
        
        if cnt >= n:
            right = mid-1
            answer=mid
        else:
            left = mid+1
    
    return answer