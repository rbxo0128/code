from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)

        answer = -1
        if k == 1:
            for x,c in cnt.items():
                if c == 1:
                    answer = max(answer, x)

        elif k == len(nums):
            answer = max(nums)

        else:
            if nums[0] in cnt:
                if cnt[nums[0]] == 1:
                    answer = max(answer, nums[0])

            if nums[-1] in cnt:
                if cnt[nums[-1]] == 1:
                    answer = max(answer, nums[-1])

        return answer