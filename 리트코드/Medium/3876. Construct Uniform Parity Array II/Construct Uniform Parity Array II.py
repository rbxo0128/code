class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_num = float("inf")
        check = False
        for i in range(len(nums1)):
            min_num = min(min_num, nums1[i])
            if nums1[i] % 2 == 1:
                check = True

        if not check:
            return True

        if min_num % 2 == 1:
            return True

        return False