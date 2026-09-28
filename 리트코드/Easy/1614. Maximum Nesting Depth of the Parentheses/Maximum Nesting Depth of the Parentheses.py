class Solution:
    def maxDepth(self, s: str) -> int:
        answer = 0
        tmp = 0
        for x in s:
            if x == "(":
                tmp += 1
                answer = max(tmp, answer)

            elif x == ")":
                tmp -= 1           

        return answer