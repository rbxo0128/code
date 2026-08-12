from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        counts = defaultdict(int)
        answer = 0

        while right != n:
            counts[nums[right]] += 1
            while counts[nums[right]] > k:
                counts[nums[left]] -= 1
                left += 1

            right += 1
            answer = max(answer, right - left)

        return answer
