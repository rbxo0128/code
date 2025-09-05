import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

parents = {}
def find(x):
    if x not in parents:
        parents[x] = x

    if parents[x] != x:
        parents[x] = find(parents[x])

    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if not a == b:
        parents[a] = b

n,m = map(int, input().split())

arr = []
for i in range(m):
    x,y,w = map(int, input().split())
    arr.append([w,x,y])

arr.sort()

answer = 0
for w,x,y in arr:
    if not find(x) == find(y):
        union(x,y)
        answer += w

print(answer)