class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        answer = 0

        if need1 < need2:
            need1,need2 = need2,need1
            cost1,cost2 = cost2,cost1

        same = min(need1,need2)

        answer += same * min(cost1+cost2,costBoth)
        need1 -= same

        answer += need1 * min(cost1, costBoth)

        return answer