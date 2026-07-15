class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left = 0
        right = len(height) - 1

        while left < right:
            answer = max(answer,(right-left) * min(height[left],height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return answer


# 100000