class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        INF = float("inf")
        dp = [INF] * (n)

        dp[0] = 1+costs[0]
        if n == 1:
            return dp[0]
        dp[1] = min(4,dp[0]+1)+costs[1]
        if n == 2:
            return dp[1]
        dp[2] = min(9,dp[0]+4,dp[1]+1)+costs[2]
        if n == 3:
            return dp[2]

        for i in range(3,n):
            dp[i] = min(dp[i-3]+9,dp[i-2]+4,dp[i-1]+1)+costs[i]
        
        return dp[-1]