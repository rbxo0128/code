class Solution:
    def countCommas(self, n: int) -> int:
        answer = 0
        check = 1000

        while check <= n:
            answer += (n - check + 1)
            check *= 1000

        return answer



#1,000
#1,000,000
#1,000,000,000