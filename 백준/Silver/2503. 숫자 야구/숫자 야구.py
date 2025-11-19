import sys

input = sys.stdin.readline

n = int(input())
op = []
for _ in range(n):
    num, s, b = map(int, input().split())
    op.append((str(num), s, b))

answers = [x for x in range(100,1000) if not (str(x)[0] == str(x)[1] or str(x)[1] == str(x)[2] or str(x)[0] == str(x)[2]) and not "0" in str(x)]

result = 0
for answer in answers:
    isAnswer = True
    for num, s, b in op:
        strike = sum([str(answer)[i] == num[i] for i in range(3)])
        ball = len(set(str(answer)) & set(num)) - strike
        if strike != s or ball != b:
            isAnswer = False
            break
    if isAnswer:
        result += 1
        
print(result)