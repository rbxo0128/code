import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = 0
        prefixGcd = []
        for i in range(n):
            mx = max(mx, nums[i])
            prefixGcd.append(math.gcd(mx,nums[i]))

        left = 0
        right = n - 1
        answer = 0
        prefixGcd.sort()
        while left < right:
            answer += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return answer