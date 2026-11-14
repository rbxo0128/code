class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        answer = float("inf")
        n = len(nums)

        for i in range(l,r+1):
            total = sum(nums[:i])

            if total > 0:
                answer = min(answer, total)

            for j in range(i, n):
                total -= nums[j-i]
                total += nums[j]

                if total > 0:
                    answer = min(answer, total)

        return answer if answer != float("inf") else -1