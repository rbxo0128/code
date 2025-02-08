
def solution(m, n, startX, startY, balls):
    startX_c1 = -startX
    startX_c2 = startX+(m-startX)*2
    startY_c1 = -startY
    startY_c2 = startY+(n-startY)*2
    
    result=[]
    for i in balls:
        x,y = i
        if x == startX:
            a=(x-startX_c1)**2+(y-startY)**2
            b=(x-startX_c2)**2+(y-startY)**2
            if y>startY:
                c=(x-startX)**2+(y-startY_c1)**2
                d=(x-startX)**2+(y-startY_c1)**2
            else:
                c=(x-startX)**2+(y-startY_c2)**2
                d=(x-startX)**2+(y-startY_c2)**2
        
        elif y==startY:
            if x>startX:
                a=(x-startX_c1)**2+(y-startY)**2
                b=(x-startX_c1)**2+(y-startY)**2
            else:
                a=(x-startX_c2)**2+(y-startY)**2
                b=(x-startX_c2)**2+(y-startY)**2
            c=(x-startX)**2+(y-startY_c1)**2
            d=(x-startX)**2+(y-startY_c2)**2
        else:
            a=(x-startX_c1)**2+(y-startY)**2
            b=(x-startX_c2)**2+(y-startY)**2
            c=(x-startX)**2+(y-startY_c1)**2
            d=(x-startX)**2+(y-startY_c2)**2
        result.append(min(a,b,c,d))
    print(result)
    answer = []
    return result