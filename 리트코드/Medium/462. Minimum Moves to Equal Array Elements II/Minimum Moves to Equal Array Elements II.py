class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        
        nums.sort()
        x = nums[n//2]

        answer = 0
        for num in nums:
            answer += abs(x-num)

        return answer