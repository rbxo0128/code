import sys

input = sys.stdin.readline

parent = {}
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a!=b:
        parent[a] = b

g = int(input())
p = int(input())

parent = [i for i in range(g+1)]

result = 0
for i in range(p):
    air = int(input())
    x = find(air)
    if x == 0:
        break
    union(x, x-1)
    result += 1

print(result)