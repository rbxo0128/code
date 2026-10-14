class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        answer = []
        for i in range(num):
            if sum >= 9:
                answer.append(9)
                sum -= 9
            else:
                answer.append(sum)
                sum -= sum

        return "".join(map(str,answer))