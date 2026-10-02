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
                DFS(stack+[")"],cnt-1,level+1)

            if 2*n - level > cnt:
                DFS(stack+["("],cnt+1, level+1)
        
        DFS([],0,0)
        
        return answer