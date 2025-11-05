import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    exit()

dp = [0 for i in range(n)]
    
dp[0] = 1
dp[1] = 2

for i in range(2,n):
    dp[i] = (dp[i-1]%15746 + dp[i-2]%15746)%15746

print(dp[-1])