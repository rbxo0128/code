from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)

        c = sorted(count.items())
        answer = []
        mid = ""

        tmp_y = 0
        for x,y in c:
            for i in range(y//2):
                answer.append(x)

            if y % 2 == 1:
                mid = x

        tmp_reverse = answer[::-1]
        if mid:
            answer.append(mid)

        return ''.join(answer + tmp_reverse)