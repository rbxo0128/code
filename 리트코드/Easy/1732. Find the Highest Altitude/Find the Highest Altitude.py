class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]
        for i in range(len(gain)):
            arr.append(arr[i] + gain[i])

        return max(arr)