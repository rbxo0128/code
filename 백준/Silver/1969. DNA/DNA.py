import sys
from collections import defaultdict

input = sys.stdin.readline

n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(input().strip()))

answer_word = []
answer_num = 0
for j in range(m):
    d = defaultdict(int)
    for i in range(n):
        d[arr[i][j]] += 1

    for x,y in sorted(d.items(), key= lambda x:(-x[1],x[0])):
        answer_num += n-y
        answer_word.append(x)
        break

print("".join(answer_word))
print(answer_num)