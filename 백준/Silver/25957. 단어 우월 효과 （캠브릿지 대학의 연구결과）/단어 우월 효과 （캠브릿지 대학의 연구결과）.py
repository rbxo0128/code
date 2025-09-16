import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
original = {}
for i in range(n):
    word = input().strip()
    if len(word) <= 2:
        key = word
    else:
        key = word[0] + ''.join(sorted(word[1:-1])) + word[-1]
    original[key] = word

m = int(input())
edit = list(input().split())
answer = []
for word in edit:
    if len(word) <= 2:
        key = word
    else:
        key = word[0] + ''.join(sorted(word[1:-1])) + word[-1]
    answer.append(original[key])

print(' '.join(answer))