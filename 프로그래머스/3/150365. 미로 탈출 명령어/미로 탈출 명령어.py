def solution(n, m, x, y, r, c, k):
    answer = ''
    cnt = 0
    for i in range(k):
        print(x,y)
        if check(n,m,x+1,y,r,c,k,cnt+1):
            x+=1
            cnt += 1
            answer += 'd'
            continue
        elif check(n,m,x,y-1,r,c,k,cnt+1):
            y-=1
            cnt += 1
            answer += 'l'
            continue
        
        elif check(n,m,x,y+1,r,c,k,cnt+1):
            y+=1
            cnt += 1
            answer += 'r'
            continue

        elif check(n,m,x-1,y,r,c,k,cnt+1):
            x-=1
            cnt += 1
            answer += 'u'
            continue
        
        return "impossible"
        
    
    return answer

def check(n,m,x,y,r,c,k,cnt):
    least = abs(r-x)+abs(c-y)
    if 0<x<=n and 0<y<=m:
        if ((k-least-cnt)%2 == 0) and k >= least+cnt:
            return True
        
    return False

        



# d 로 이동 체크 가능하면 이동
# r 로 이동 체크 가능하면 이동 