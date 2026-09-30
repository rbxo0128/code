class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        cnt = 0
        answer = []
        for x in seq:
            if x == "(":
                if cnt % 2 == 1:
                    answer.append(1)
                else:
                    answer.append(0)
                cnt += 1
            else:
                cnt -= 1
                if cnt % 2 == 1:
                    answer.append(1)
                else:
                    answer.append(0)
     
        return answer