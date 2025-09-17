import sys
input = sys.stdin.readline

n = int(input())

words = input().strip()
dp = [[float("inf"), -1] for i in range(n)]
dp[0][0] = 0
dp[0][1] = 0

boj = ["B", "O", "J"]
idx = 0
j = 0
for i in range(1,n):
    for j in range(0,i):
        if dp[i][0] > dp[j][0] + (i-j) ** 2 and words[i] == boj[(dp[j][1]+1)%3]:
            dp[i] = [dp[j][0] + (i-j) ** 2, (dp[j][1]+1)%3]

if dp[-1][0] == float("inf"):
    print(-1)
else:
    print(dp[-1][0])