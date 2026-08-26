class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        right = 0

        cnt = 0

        answer = []
        while right != len(s):
            if s[right] == "1":
                cnt += 1

            while k == cnt:
                if k == cnt and s[left] == "1":
                    answer.append(s[left:right+1])

                if s[left] == "1":
                    cnt -= 1
                left += 1

            right += 1
        
        answer.sort(key = lambda x:(len(x),x))
        return answer[0] if answer else ""