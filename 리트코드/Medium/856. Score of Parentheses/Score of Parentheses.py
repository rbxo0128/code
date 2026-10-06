class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        answer = 0
        for i,x in enumerate(s):
            if x == "(":
                stack.append("(")
            else:
                stack.pop()
                if s[i-1] == "(":
                    answer += 2 ** len(stack)

        return answer