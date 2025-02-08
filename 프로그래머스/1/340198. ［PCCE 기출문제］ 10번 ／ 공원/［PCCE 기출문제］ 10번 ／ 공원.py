def solution(mats, park):
    row = len(park)
    col = len(park[0])
    lists = [[0] *col for i in range(row)]
    result=0
    for i in range(row):
        for j in range(col):
            if park[i][j] == "-1":
                if i==0 or j==0:
                    lists[i][j] =1
                else:
                    lists[i][j] = min(lists[i-1][j], lists[i][j-1], lists[i-1][j-1]) + 1
                result = max(result, lists[i][j])
    print(lists)
    answer=0
    for i in mats:
        maxs = answer
        if i <= result and i > maxs:
            answer = i
    
    if answer ==0:
        answer = -1
    return answer