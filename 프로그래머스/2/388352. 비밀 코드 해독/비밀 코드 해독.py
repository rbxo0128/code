from itertools import combinations
from collections import deque
def solution(n, q, ans):
    arr = [i for i in range(1,n+1)]
    queue = deque(combinations(arr, 5))
    
    count = 0
    
    while queue:
        isbool = True
        a,b,c,d,e  = queue.popleft()
        index = 0
        for i in q:
            cnt = 0
            if a in set(i):
                cnt+=1
            if b in set(i):
                cnt+=1
            if c in set(i):
                cnt+=1
            if d in set(i):
                cnt+=1
            if e in set(i):
                cnt+=1
            
            if not cnt == ans[index]:
                isbool = False
                break
            index+=1
        if isbool:
            count+=1
    answer = 0
    return count