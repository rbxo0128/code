import sys

input = sys.stdin.readline

arr = []

n = int(input())

for i in range(n):
    arr.append(int(input()))


dp = [0] * (n)
dp[0] = arr[0]
if n == 1:
    print(dp[0])
    exit()
dp[1] = max(arr[1], arr[0] + arr[1] // 2, dp[0])
if n == 2:
    print(dp[1])
    exit()
dp[2] = max(dp[1], dp[0] + arr[2], arr[1] + arr[2] // 2)



for i in range(3,n):
    dp[i] = max(dp[i-1],dp[i-2] + arr[i], dp[i-3]+arr[i-1]+arr[i]//2)

print(dp[-1])