import sys

input = sys.stdin.readline

n = input().strip()
m = input().strip()

m_len = len(m)
tmp = 0
answer = 0

while tmp + m_len <= len(n):
    if n[tmp:tmp+m_len] == m:
        tmp += m_len
        answer += 1
    else:
        tmp += 1

print(answer)