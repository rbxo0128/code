class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        answer = []
        for i in range(1,10):
            s = i
            total = s
            while s < 9:
                s += 1
                total = 10*total + s

                if total > high:
                    break

                if low <= total:
                    answer.append(total)

        return sorted(answer)
