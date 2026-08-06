class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            check = 1
            for num in str(n):
                check *= int(num)
                if check % t == 0:
                    return n

            n += 1