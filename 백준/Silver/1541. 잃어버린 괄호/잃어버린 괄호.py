import sys
from collections import deque

input = sys.stdin.readline

words = input().strip()

temp = 0
result = [[]]
for idx,word in enumerate(words):
    if word == "+":
        num = int(words[temp:idx])
        result[-1].append(num)
        temp = idx+1
    elif word == "-":
        num = int(words[temp:idx])
        result[-1].append(num)
        result.append([])
        temp = idx+1
    elif idx == len(words)-1:
        num = int(words[temp:])
        result[-1].append(num)

total = 0

total = sum(result[0]) * 2
for num in result:
    total -= sum(num)

print(total)