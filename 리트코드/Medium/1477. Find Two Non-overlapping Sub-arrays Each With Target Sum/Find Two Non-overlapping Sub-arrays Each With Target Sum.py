class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        dp = [float("inf")] * n

        left = 0
        total = 0
        answer = float("inf")
        
        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                l = right - left + 1
                if left > 0 and dp[left-1] != float("inf"):
                    answer = min(answer, dp[left-1]+l)

                prev = dp[right-1] if right > 0 else float("inf")
                dp[right] = min(prev, l)
            else:
                if right > 0:
                    dp[right ] = dp[right - 1]

        return answer if answer != float("inf") else -1
