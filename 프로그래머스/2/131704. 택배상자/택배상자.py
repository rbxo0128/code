from collections import deque

def solution(order):
    stack = deque()
    answer = 0
    idx = 0
    for i in range(1,len(order)+1):
        if i == order[idx]:
            answer+=1
            idx += 1

            while stack:
                if stack[-1] == order[idx]:
                    answer += 1
                    stack.pop()
                    idx += 1
                    if idx == len(order):
                        break
                    
                else:
                    break
        else:
            stack.append(i)        
        
    return answer