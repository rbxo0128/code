import sys
input = sys.stdin.readline

n,m = map(int, input().split())

list = []

for i in range(m):
    x,y = map(int, input().split())
    list.append((x,y))

mx = sorted(list)[m//2][0]
my = sorted(list, key=lambda x:x[1])[m//2][1]

total = 0
for x,y in list:
    total += abs(x-mx)+abs(y-my)

print(total)