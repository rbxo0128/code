class Solution:
    def longestValidParentheses(self, s: str) -> int:
        cnt = 0
        tmp = 0
        n = len(s)
        answer = 0
        for i in range(n):
            if s[i] == '(':
                cnt += 1
            else:
                cnt -= 1

            if cnt == 0:
                answer = max(answer, i - tmp + 1)

            elif cnt < 0:
                cnt = 0
                tmp = i + 1

        cnt = 0
        tmp = n - 1

        for i in range(n - 1, -1, -1):
            if s[i] == ')':
                cnt += 1
            else:
                cnt -= 1

            if cnt == 0:
                answer = max(answer, tmp - i + 1)

            elif cnt < 0:
                cnt = 0
                tmp = i - 1

        return answer