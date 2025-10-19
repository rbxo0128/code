import sys

input = sys.stdin.readline

t = int(input())


for i in range(t):
    x,y = map(int,input().split())
    arr = set()
    while x:
        arr.add(x)
        x //= 2

    while y:
        if y in arr:
            print(y*10)
            break

        y //= 2