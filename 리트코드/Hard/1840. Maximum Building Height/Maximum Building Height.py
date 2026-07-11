class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        restrictions.sort()

        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (id2 - id1))

        for i in range(len(restrictions) - 2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            restrictions[i][1] = min(h1, h2 + (id2 - id1))

        answer = 0
        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]

            answer = max(answer, (id2 - id1 + h1 + h2) // 2)

        return answer