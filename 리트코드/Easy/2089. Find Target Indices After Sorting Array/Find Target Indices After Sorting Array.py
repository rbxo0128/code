class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        idx = 0
        cnt = 0
        for num in nums:
            if num < target:
                idx += 1

            elif num == target:
                cnt += 1

        return [idx+i for i in range(cnt)]