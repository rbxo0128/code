class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        answer = 0
        n = len(arr2)
        arr2.sort()

        for x in arr1:
            left = 0
            right = n-1
            idx = n

            while left<=right:
                mid = (left+right) // 2
                if arr2[mid] >= x:
                    idx = mid
                    right = mid-1
                else:
                    left = mid+1

            check = False
            if idx<n and abs(arr2[idx]-x) <= d:
                check = True
            if idx>0 and abs(arr2[idx-1]-x) <= d:
                check = True

            if not check:
                answer += 1

        return answer