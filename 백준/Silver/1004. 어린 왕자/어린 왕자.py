import sys

t = int(sys.stdin.readline())

for i in range(t):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    stack1 = []
    stack2 = []
    for i in range(n):
        dx,dy,dr = map(int, sys.stdin.readline().split())
        dist1 = (x1-dx)**2+(y1-dy)**2
        dist2 = (x2-dx)**2+(y2-dy)**2
        if (dr**2 > dist1):
            stack1.append(i)
        if(dr**2 > dist2):
            stack2.append(i)

    answer = len(stack1) + len(stack2)
    for i in stack1:
        if i in stack2:
            answer-=2
    
    print(answer)