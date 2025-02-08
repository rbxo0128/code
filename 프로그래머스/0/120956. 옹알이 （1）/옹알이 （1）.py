def solution(babbling):
    a = ''.join(babbling)
    answer = 0
    for i in babbling:
        a = i.replace('aya','1')
        a = a.replace('ye','1')
        a = a.replace('woo','1')
        a = a.replace('ma','1')
        if a.isdigit():
            answer+=1
    
    return answer