# 풀이: 길이 x인 각 구간을 중앙값으로 맞추는 비용을 계산한 뒤,
# DP로 서로 겹치지 않는 k개 구간을 선택해 최소 연산 횟수를 구한다.
# 결과: 시간 초과(TLE)
# 원인: 매 구간을 다시 정렬하고 비용을 계산해 O(n * x * log x)의 시간이 걸린다.

from collections import deque

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        right= x-1
        arr = []
        new_nums = deque(nums[:right+1])

        while True:
            tmp = sorted(new_nums)
            total = 0
            for i in tmp:
                total += abs(i-tmp[x//2])
            
            arr.append(total)
            if right + 1 >= n:
                break
            new_nums.popleft()
            right+=1
            new_nums.append(nums[right])
        
        INF = float('inf')
        dp = [[INF] * (n + 1) for i in range(k + 1)]
        
        for i in range(n + 1):
            dp[0][i] = 0

        for j in range(1, k+1):
            for i in range(j*x, n+1):
                skip = dp[j][i-1]
                select = dp[j-1][i-x] + arr[i-x]

                dp[j][i] = min(skip, select)

        return dp[k][n]
