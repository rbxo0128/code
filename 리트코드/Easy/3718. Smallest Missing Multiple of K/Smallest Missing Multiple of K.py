class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)

        idx = 1
        while True:
            if k * idx in nums_set:
                idx += 1
                continue

            else:
                return k * idx