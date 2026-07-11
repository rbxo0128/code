class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        C = [0] * (max_cost+1)
        for i in range(len(costs)):
            C[costs[i]] += 1

        count = 0
        for i in range(1,max_cost+1):
            if C[i] == 0:
                continue

            can_buy = min(C[i], coins // i)

            coins -= can_buy * i
            count += can_buy

            if coins < i:
                break

        return count

        