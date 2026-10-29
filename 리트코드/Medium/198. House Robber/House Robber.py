class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1,n):
            if i == 1:
                dp[i] = max(dp[0],nums[1])
                continue

            dp[i] = max(dp[i-2]+nums[i],dp[i-1])

        return dp[-1]