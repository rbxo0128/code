import re

def solution(user_id, banned_id):
    
    bans = []
    for pattern in banned_id:
        regex = re.compile("^" + pattern.replace("*", ".") + "$")
        ban = []
        for w in user_id:
            if regex.fullmatch(w):
                ban.append(w)
            
        bans.append(ban)
        
    l = len(banned_id)
    banned = set()
    
    def DFS(level, target):
        if level == l:
            banned.add(tuple(sorted(target)))
            return
            
        for i in bans[level]:
            if i not in target:
                DFS(level+1,target | {i})
    
    DFS(0,set())
        
    return len(banned)