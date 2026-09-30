class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        cnt = 0
        level = []
        for x in seq:
            if x == "(":
                level.append(cnt)
                cnt += 1
            else:
                cnt -= 1
                level.append(cnt)

        answer = []
        for x in level:
            if x % 2 == 1:
                answer.append(0)

            else:
                answer.append(1)
        
        return answer