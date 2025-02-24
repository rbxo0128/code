import sys
import heapq



n= int(sys.stdin.readline())


for i in range(n):
    stack = []
    words = sys.stdin.readline().strip()
    isbool = True
    for word in words:
        if word == "(":
            stack.append(word)
        else:
            if stack:
                stack.pop()
            else:
                isbool = False
                break
    
    if not isbool or stack:
        print("NO")

    if isbool and not stack:
        print("YES")