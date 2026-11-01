class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_num = min(nums)
        answer = 0
        for num in nums:
            answer += num - min_num

        return answer        


