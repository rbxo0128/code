import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)
        c = sorted(count.items())
        
        answer = []
        mid = ""
        
        half_dict = {}
        n = 0
        
        for x, y in c:
            if y // 2 > 0:
                half_dict[x] = y // 2
                n += y // 2
            if y % 2 == 1:
                mid = x
                
        p = math.factorial(n)
        for x,y in half_dict.items():
            p //= math.factorial(y)
            
        if p < k:
            return ""
            
        while n > 0:
            for x in sorted(half_dict.keys()):
                y = half_dict[x]
                if y > 0:
                    w = p * y // n
                    
                    if k <= w:
                        answer.append(x)
                        half_dict[x] -= 1
                        p = w
                        n -= 1
                        break
                    else:
                        k -= w
                        
        tmp_reverse = answer[::-1]
        if mid:
            answer.append(mid)
            
        return ''.join(answer + tmp_reverse)