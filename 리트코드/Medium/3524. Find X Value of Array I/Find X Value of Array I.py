class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        answer = [0] * k
        dp = [0] * k

        for x in nums:
            v = x % k
            n = [0] * k
            n[v] += 1
            for i in range(k):
                if dp[i]:
                    n[(i * v) % k] += dp[i]

            dp = n
            for i in range(k):
                answer[i] += dp[i]

        return answer