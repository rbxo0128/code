def solution(dirs):
    x,y = 0,0
    check = set()
    for op in dirs:
        if op == "U":
            if -5<= y+1 <= 5:
                if (x,y,x,y+1) not in check:
                    check.add((x,y,x,y+1))
                y+=1
                
        elif op == "D":
            if -5<= y-1 <= 5:
                if (x,y-1,x,y) not in check:
                    check.add((x,y-1,x,y))
                y-=1
        elif op == "L":
            if -5<= x-1 <= 5:
                if (x-1,y,x,y) not in check:
                    check.add((x-1,y,x,y))
                x-=1
        elif op == "R":
            if -5<= x+1 <= 5:
                if (x,y,x+1,y) not in check:
                    check.add((x,y,x+1,y))
                x+=1
                
    return len(check)