class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda x:x[1])
        for i in range(len(queries)):
            queries[i] = [i,queries[i]]

        queries.sort(key = lambda x:x[1])
        
        left=0
        right=0
        cnt=[0]*(n+1)
        total=0
        arr=[0]*len(queries)

        for idx, query in queries:
            while right < len(logs) and logs[right][1] <= query:
                server = logs[right][0]

                if cnt[server] == 0:
                    total += 1

                cnt[server] += 1
                right += 1

            while left < right and logs[left][1] < query - x:
                server = logs[left][0]
                cnt[server] -= 1

                if cnt[server] == 0:
                    total -= 1
                left += 1

            arr[idx] = n-total

        return arr