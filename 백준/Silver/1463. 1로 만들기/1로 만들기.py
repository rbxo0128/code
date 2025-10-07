import sys
n = int(sys.stdin.readline())
dp1 = [0 for i in range(1000001)]
for i in range(2, 1000001):
    dp1[i] = dp1[i - 1] + 1

    if i % 2 == 0:
        dp1[i] = min(dp1[i], dp1[i // 2] + 1)

    if i % 3 == 0:
        dp1[i] = min(dp1[i], dp1[i // 3] + 1)
        
print(dp1[n])