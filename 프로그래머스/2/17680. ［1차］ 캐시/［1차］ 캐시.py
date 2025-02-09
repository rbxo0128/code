from collections import deque
def solution(cacheSize, cities):
    arr = deque()
    count = 0
    arr_set = set()
    if cacheSize == 0:
        return len(cities)*5
    
    for i in cities:
        ii = i.lower()
        if ii in arr_set:
                arr.remove(ii)
                arr.append(ii)
                count+=1
        else:
            if len(arr) < cacheSize:
                arr.append(ii)
                arr_set.add(ii)
                count+=5

            else:
                x = arr.popleft()
                arr.append(ii)

                arr_set.discard(x)
                arr_set.add(ii)

                count+=5
                
    return count

