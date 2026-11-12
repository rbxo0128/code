class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        up = 1
        down = 1
        answer = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up += 1
                down = 1
            elif nums[i] < nums[i-1]:
                down += 1
                up = 1
            else:
                up = 1
                down = 1

            answer = max(answer, up, down)

        return answer