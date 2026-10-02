class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        answer = []
        def DFS(stack, cnt, level):
            nonlocal answer
            if level == 2*n:
                if cnt == 0:
                    answer.append("".join(stack))
                    return

            if cnt > 0:
                stack.append(")")
                DFS(stack,cnt-1,level+1)
                stack.pop()

            if 2*n - level > cnt:
                stack.append("(")
                DFS(stack,cnt+1, level+1)
                stack.pop()
        
        DFS([],0,0)
        
        return answer