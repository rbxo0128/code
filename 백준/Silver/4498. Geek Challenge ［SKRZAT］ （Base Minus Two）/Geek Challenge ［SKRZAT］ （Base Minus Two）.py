import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

def dtob(x):
    num = int(x)
    if num == 0:
        print("From decimal: 0 is 0")
        return
    
    result = ""
    while num != 0:
        r = num % -2
        num = num // -2
        if r < 0:
            r += 2
            num += 1
        result = str(r) + result
    
    print("From decimal: " + x + " is " + result)

def btod(x):
    total = 0
    idx = 0
    for i in range(len(x)-1, -1, -1):
        total += int(x[i]) * (-2)**idx
        idx+=1

    print("From binary: " + x + " is " + str(total))

for i in range(n):
    op, num = input().split()
    
    if op == "b":
        btod(num)


    else:
        dtob(num)