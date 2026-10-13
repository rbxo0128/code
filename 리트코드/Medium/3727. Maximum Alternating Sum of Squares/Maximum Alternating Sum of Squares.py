class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x:abs(x))
        
        n = len(nums)
        answer = 0

        for i in range(n):
            if i % 2 == 0:
                answer += nums[n-1-(i//2)] ** 2

            else:
                answer -= nums[i//2] ** 2

        return answer