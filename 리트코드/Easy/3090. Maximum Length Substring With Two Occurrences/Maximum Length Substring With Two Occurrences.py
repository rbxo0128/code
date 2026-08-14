class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        k = 2
        left = 0
        right = 0
        counts = defaultdict(int)
        answer = 0

        while right != n:
            counts[s[right]] += 1
            while counts[s[right]] > k:
                counts[s[left]] -= 1
                left += 1

            right += 1
            answer = max(answer, right - left)

        return answer