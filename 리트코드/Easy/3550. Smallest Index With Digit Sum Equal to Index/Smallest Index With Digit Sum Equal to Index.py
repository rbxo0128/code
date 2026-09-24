class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            total = 0
            for x in str(num):
                total += int(x)

            if i == total:
                return i

        return -1
