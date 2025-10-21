from collections import deque

def solution(prices):
    n = len(prices)
    arr = [0 for i in range(n)]
    stack = deque()
    for i in range(n):
        for j in range(len(stack)):
            x,index,cnt = stack.popleft()
            if x > prices[i]:
                arr[index] = cnt
            else:
                stack.append((x,index,cnt+1))
        stack.append((prices[i],i,1))       
    
    for x,index,cnt in stack:
        arr[index] = cnt-1
                
    return arr