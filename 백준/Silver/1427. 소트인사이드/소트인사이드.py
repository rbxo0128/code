import sys

num = list(sys.stdin.readline().strip())

num.sort(reverse=True)
print(''.join(num))

