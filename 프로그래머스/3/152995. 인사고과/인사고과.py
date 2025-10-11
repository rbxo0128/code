def solution(scores):
    m_x,m_y = scores[0][0], scores[0][1]
    me = m_x+m_y
    scores.sort(reverse=True, key=lambda x:(x[0],-x[1]))
    
    temp = 0
    result = []
    for x,y in scores:
        temp = max(y,temp)
        if y < temp:
            if m_x == x and m_y == y:
                return -1
            continue
            
        result.append(x+y)
    
    result.sort(reverse=True)
    answer = result.index(me)
    return answer+1
