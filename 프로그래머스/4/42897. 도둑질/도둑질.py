def solution(money):
    x = len(money)
    dp = [0 for i in range(x)]
    dp[0] = money[0]
    dp[1] = money[1]
    dp[2] = money[0] + money[2]
    for i in range(3,x-1):
        dp[i] = max(dp[i-2],dp[i-3])+money[i]
    
    dp1 = [0 for i in range(x)]
    dp1[0] = 0
    dp1[1] = money[1]
    dp1[2] = money[2]
    
    for i in range(3,x):
        dp1[i] = max(dp1[i-2],dp1[i-3])+money[i]
    
    
    answer = 0
    return max(max(dp),max(dp1))