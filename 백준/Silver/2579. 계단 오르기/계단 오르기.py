import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

if len(arr) <= 2:
    print(sum(arr))

else:
    dp = [0 for i in range(n)]
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])

    for i in range(3,n):
        dp[i] = max(arr[i]+arr[i-1]+dp[i-3], arr[i]+dp[i-2])

    print(dp[-1])