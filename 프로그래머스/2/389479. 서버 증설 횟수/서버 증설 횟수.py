from collections import deque

def solution(players, m, k):
    answer = 0
    stack = deque()
    for i in range(k):
        stack.append(0)
    
    for i in players:
        a = i//m
        
        server = stack.popleft()
        stack.append(0)
        
        if a >= server:
            increase = a - server
            answer += increase
            for i in range(k-1):
                stack[i] += increase
        
            
    return answer