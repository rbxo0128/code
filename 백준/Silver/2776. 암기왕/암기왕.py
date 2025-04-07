import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())

    set1 = set(map(int,sys.stdin.readline().split()))

    m = int(sys.stdin.readline())

    for i in list(map(int,sys.stdin.readline().split())):
        if i in set1:
            print(1)
        else:
            print(0)

