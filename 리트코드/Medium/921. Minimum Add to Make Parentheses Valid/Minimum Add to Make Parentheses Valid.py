class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        answer = 0
        for x in s:
            if x == "(":
                cnt += 1

            else:
                cnt -= 1

            if cnt < 0:
                answer += 1
                cnt = 0

        answer += cnt
        return answer