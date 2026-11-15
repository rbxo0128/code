class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd = 0
        even = 0
        answer = 0
        for num in arr:
            if num%2 == 0:
                even+=1
            else:
                odd,even=even+1,odd

            answer+=odd

        return answer%(10**9 + 7)