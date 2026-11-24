import sys
from collections import deque

input = sys.stdin.buffer.readline

def solve():
    N, K = map(int, input().split())
    NN = N * N

    # grid[idx] = 0(미개) or 문명 id
    grid = [0] * NN

    parent = list(range(K + 1))
    size = [1] * (K + 1)
    components = K

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        nonlocal components
        a = find(a); b = find(b)
        if a == b:
            return
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
        components -= 1

    q = deque()
    seeds = []

    # 입력: 발상지 배치
    for cid in range(1, K + 1):
        x, y = map(int, input().split())
        x -= 1; y -= 1
        idx = x * N + y
        grid[idx] = cid
        q.append(idx)
        seeds.append(idx)

    # 초기(0년) 인접 발상지는 바로 결합
    for idx in seeds:
        x = idx // N
        y = idx - x * N
        cid = grid[idx]

        if x > 0:
            nb = grid[idx - N]
            if nb:
                union(cid, nb)
        if x < N - 1:
            nb = grid[idx + N]
            if nb:
                union(cid, nb)
        if y > 0:
            nb = grid[idx - 1]
            if nb:
                union(cid, nb)
        if y < N - 1:
            nb = grid[idx + 1]
            if nb:
                union(cid, nb)

    if components == 1:
        print(0)
        return

    year = 0

    while components > 1:
        # 1) 합치기 단계: 현재 frontier끼리 인접하면 union (같은 해 결합을 정확히 처리)
        qs = len(q)
        for _ in range(qs):
            idx = q.popleft()
            x = idx // N
            y = idx - x * N

            cid = find(grid[idx])

            if x > 0:
                nb = grid[idx - N]
                if nb:
                    union(cid, nb)
            if x < N - 1:
                nb = grid[idx + N]
                if nb:
                    union(cid, nb)
            if y > 0:
                nb = grid[idx - 1]
                if nb:
                    union(cid, nb)
            if y < N - 1:
                nb = grid[idx + 1]
                if nb:
                    union(cid, nb)

            q.append(idx)

        if components == 1:
            print(year)
            return

        # 2) 확산 단계: frontier에서 빈칸 확장, 다른 문명 만나면 union
        next_q = deque()
        qs = len(q)
        for _ in range(qs):
            idx = q.popleft()
            x = idx // N
            y = idx - x * N

            cid = find(grid[idx])

            # 상
            if x > 0:
                nidx = idx - N
                v = grid[nidx]
                if v == 0:
                    grid[nidx] = cid
                    next_q.append(nidx)
                else:
                    union(cid, v)

            # 하
            if x < N - 1:
                nidx = idx + N
                v = grid[nidx]
                if v == 0:
                    grid[nidx] = cid
                    next_q.append(nidx)
                else:
                    union(cid, v)

            # 좌
            if y > 0:
                nidx = idx - 1
                v = grid[nidx]
                if v == 0:
                    grid[nidx] = cid
                    next_q.append(nidx)
                else:
                    union(cid, v)

            # 우
            if y < N - 1:
                nidx = idx + 1
                v = grid[nidx]
                if v == 0:
                    grid[nidx] = cid
                    next_q.append(nidx)
                else:
                    union(cid, v)

        q = next_q
        year += 1

    print(year)

if __name__ == "__main__":
    solve()
