import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd, sumEven = 0,0
        for i in range(1,2*n+1):
            if i % 2 == 1:
                sumOdd += i
                continue
            
            sumEven += i

        return math.gcd(sumOdd,sumEven)