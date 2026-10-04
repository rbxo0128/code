class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt = 0
        for x in s:
            if x == ")":
                cnt -= 1
            else:
                cnt += 1
            
            if cnt < 0:
                return False

        cnt = 0
        for x in reversed(s):
            if x == "(":
                cnt -= 1
            else:
                cnt += 1

            if cnt < 0:
                return False

        return True