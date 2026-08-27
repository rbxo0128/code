from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        for i in target:
            cnt[i] -= 1
            
        for i in range(n - 1, -1, -1):
            cnt[target[i]] += 1
            
            if any(x < 0 for x in cnt.values()):
                continue
            
            for c in range(ord(target[i]) + 1, ord('z') + 1):
                ch = chr(c)
                if cnt[ch] > 0:
                    cnt[ch] -= 1
                    rest = "".join(chr(k) * cnt[chr(k)] for k in range(ord('a'), ord('z') + 1) if cnt[chr(k)] > 0)
                    
                    return target[:i] + ch + rest
                    
        return ""