import math
from collections import deque

def solution(progresses, speeds):
    
    result = deque()
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        day = math.ceil(remain / speeds[i])
        result.append(day)
    
    answer = []
    print(result)

    while result:
        a = result.popleft()
        count = 1
        while result and result[0] <= a:
            result.popleft()
            count += 1

        answer.append(count)
        
    return answer