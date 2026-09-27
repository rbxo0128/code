class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for x in s:
            if x == ")":
                arr = []
                while stack and stack[-1] != "(":
                    arr.append(stack.pop())

                stack.pop()
                stack += arr
            else:
                stack.append(x)

        return "".join(stack)