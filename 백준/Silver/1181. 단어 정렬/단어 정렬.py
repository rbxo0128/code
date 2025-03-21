import sys


n = int(sys.stdin.readline())

words = []

for i in range(n):
    words.append(sys.stdin.readline().strip())

words.sort(key= lambda x: (len(x),x))

tmp = ""
for word in words:
    if tmp == word:
        continue
    print(word)
    tmp = word