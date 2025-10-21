import sys

input = sys.stdin.readline

n,m = map(int, input().split())

x = list(map(int, input().split()))

knows = set(x[1:])
parents = [i for i in range(n + 1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a, b = find(a), find(b)
    if a != b:
        parents[b] = a

parties = []
for i in range(m):
    x = list(map(int, input().split()))
    members = x[1:]
    parties.append(members)

    for i in range(1, len(members)):
        union(members[0], members[i])

knows = set(find(t) for t in knows)

answer = 0
for party in parties:
    for x in party:
        if find(x) in knows:
            break
    else:
        answer += 1

print(answer)