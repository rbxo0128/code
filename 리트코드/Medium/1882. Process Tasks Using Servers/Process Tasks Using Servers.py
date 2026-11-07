import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        arr = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(arr)

        work = []
        answer = []
        time = 0

        for j, task in enumerate(tasks):
            time = max(time, j)

            while work and work[0][0] <= time:
                end, w, i = heapq.heappop(work)
                heapq.heappush(arr, (w, i))

            if not arr:
                time = work[0][0]

                while work and work[0][0] <= time:
                    end, w, i = heapq.heappop(work)
                    heapq.heappush(arr, (w, i))

            w, i = heapq.heappop(arr)
            answer.append(i)

            heapq.heappush(work, (time + task, w, i))

        return answer