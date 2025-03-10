def solution(clothes):
    cloth = {}
    for x,y in clothes:
        if y in cloth:
            cloth[y].append(x)
        else:
            cloth[y] = [x]
    if len(cloth) == 1:
        for i in cloth:
            return len(cloth[i])
    else:
        answer = 1
        for i in cloth:
            answer *= len(cloth[i])+1
            
        return answer-1