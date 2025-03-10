def solution(participant, completion):
    part = {}
    for i in participant:
        if i in part:
            part[i] += 1
        else:
            part[i] = 1
            
    for i in completion:
        if i in part:
            part[i] -= 1
            
    answer = ''
    for i in part:
        if part[i] > 0:
            answer += i
    
    return answer