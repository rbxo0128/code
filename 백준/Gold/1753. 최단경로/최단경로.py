import heapq
import sys

# 입력 받기
input = sys.stdin.read
data = input().splitlines()

V, E = map(int, data[0].split())  # 정점 수 V, 간선 수 E
K = int(data[1]) - 1  # 시작 정점 K (0-based index)
graph = [[] for _ in range(V)]  # 각 정점에 대한 인접 리스트

# 간선 정보 입력 받기
for i in range(2, 2 + E):
    u, v, w = map(int, data[i].split())
    graph[u - 1].append((v - 1, w))  # (목적지, 가중치)

# 다익스트라 알고리즘을 위한 거리 배열
dist = [float('inf')] * V
dist[K] = 0  # 시작점은 거리 0

# 우선순위 큐 초기화 (가장 작은 거리부터 우선 처리)
pq = []
heapq.heappush(pq, (0, K))  # (거리, 정점)

while pq:
    current_dist, current_node = heapq.heappop(pq)  # 가장 작은 거리를 가진 노드

    # 현재 노드의 거리 값이 이미 더 작은 값이 있다면 넘어감
    if current_dist > dist[current_node]:
        continue
    
    # 인접한 노드들 확인
    for neighbor, weight in graph[current_node]:
        new_dist = current_dist + weight
        
        # 더 작은 거리로 갱신 가능하면 업데이트
        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist
            heapq.heappush(pq, (new_dist, neighbor))

# 결과 출력
for d in dist:
    # 도달할 수 없는 경우에는 'INF' 출력
    print(d if d != float('inf') else "INF")
