import sys


n = int(sys.stdin.readline())

stack = []
for i in range(n):
    try:
        a = sys.stdin.readline().split()
        x,y = int(a[0]), int(a[1])
    except:
        x = int(a[0])

    if x == 1:
        stack.append(y)
    elif x == 2:
        if(stack):
            print(stack.pop())
        else:
            print(-1)
    elif x == 3:
        print(len(stack))
    elif x == 4:
        if(stack):
            print(0)
        else:
            print(1)
    elif x == 5:
        if(stack):
            print(stack[-1])
        else:
            print(-1)

