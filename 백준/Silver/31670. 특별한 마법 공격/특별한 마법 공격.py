import sys
input = sys.stdin.readline

n= int(input())

arr = list(map(int, input().split()))

dp = [[0]*2 for i in range(n)]

dp[0][0] = 0
dp[0][1] = arr[0]

for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + arr[i]

print(min(dp[n-1][0], dp[n-1][1]))