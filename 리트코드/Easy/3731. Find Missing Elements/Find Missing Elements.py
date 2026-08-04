class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        visited =set()
        min_num = float("inf")
        max_num = 0
        for num in nums:
            visited.add(num)
            min_num = min(min_num,num)
            max_num = max(max_num,num)

        answer = []
        for i in range(min_num,max_num):
            if not i in visited:
                answer.append(i)

        return answer