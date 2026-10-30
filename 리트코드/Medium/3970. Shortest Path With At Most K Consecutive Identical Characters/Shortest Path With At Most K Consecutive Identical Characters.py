import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for i in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for i in range(n)]
        dist[0][1] = 0

        heap = [(0, 0, 1)]

        while heap:
            cost, node, cnt = heapq.heappop(heap)

            if cost > dist[node][cnt]:
                continue

            if node == n - 1:
                return cost

            for nxt, weight in graph[node]:
                if labels[node] == labels[nxt]:
                    next_cnt = cnt + 1
                else:
                    next_cnt = 1

                if next_cnt > k:
                    continue

                next_cost = cost + weight

                if next_cost < dist[nxt][next_cnt]:
                    dist[nxt][next_cnt] = next_cost
                    heapq.heappush(heap, (next_cost, nxt, next_cnt))

        return -1