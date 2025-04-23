def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        idx = 0
        fail = False
        for sk in skills:
            if sk in skill:
                if skill[idx] == sk:
                    idx+=1
                    continue
                
                fail = True
                break
        
        if not fail:
            answer+=1
            
    return answer