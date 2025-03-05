import sys

def getParent(x):
    if not parent[x] == x:
        parent[x] = getParent(parent[x])
    return parent[x]

def union(x, y):
    x = getParent(x)
    y = getParent(y)

    if not x == y:
        parent[y] = x
        friend_dict[x] += friend_dict[y]
    return friend_dict[x]

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())

    parent = {}
    friend_dict = {}

    for _ in range(m):
        fr1, fr2 = sys.stdin.readline().split()

        if fr1 not in parent:
            parent[fr1] = fr1
            friend_dict[fr1] = 1
        if fr2 not in parent:
            parent[fr2] = fr2
            friend_dict[fr2] = 1

        print(union(fr1,fr2))