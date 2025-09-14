import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

parent = {i:i for i in range(n)}
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b

arr = []
for i in range(m):
    arr.append(map(int,input().split()))

idx = 1
for x,y in arr:
    if find(x) != find(y):
        union(x,y)
        idx+=1

    else:
        print(idx)
        exit()
print(0)