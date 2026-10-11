class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            if n % (i+1) == 0:
                answer += nums[i] ** 2

        return answer