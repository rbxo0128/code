class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        answer = 0
        for num in nums:
            answer += m-num

        return answer