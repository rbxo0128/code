from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            graph[i][j] = "."
            red = (i, j)
        if graph[i][j] == "B":
            graph[i][j] = "."
            blue = (i, j)

redhole = False
bluehole = False

stack = deque([(red, blue, 0, "")])
visited = set()
visited.add((red[0], red[1], blue[0], blue[1]))
cnt = 0

dirs = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

def move_dir(r, b, cnt, ops, d):
    rx, ry = r
    bx, by = b
    dx, dy = dirs[d]

    redhole = False
    bluehole = False
    withBlue = False

    while True:
        if rx == bx and ry == by:
            withBlue = True

        cur = graph[rx][ry]
        if cur == ".":
            rx += dx
            ry += dy
        elif cur == "O":
            redhole = True
            new_red = (rx, ry)
            break
        elif cur == "#":
            new_red = (rx - dx, ry - dy)
            break

    if withBlue:
        bluehole = True
        if redhole:
            return None

        new_blue = new_red
        new_red = (new_red[0] - dx, new_red[1] - dy)

    else:
        while True:
            cur = graph[bx][by]
            if cur == ".":
                bx += dx
                by += dy
            elif cur == "O":
                bluehole = True
                break
            elif cur == "#":
                new_blue = (bx - dx, by - dy)
                break

        if redhole and not bluehole:
            return "SUCCESS", cnt + 1, ops + d

        if bluehole:
            return None

        if new_red == new_blue:
            new_blue = (new_blue[0] - dx, new_blue[1] - dy)

    moved = (new_red[0], new_red[1], new_blue[0], new_blue[1])
    if moved not in visited:
        visited.add(moved)
        stack.append((new_red, new_blue, cnt + 1, ops + d))

    return None

while stack:
    r, b, cnt, ops = stack.popleft()

    for d in ["L", "R", "U", "D"]:
        result = move_dir(r, b, cnt, ops, d)
        if result and result[0] == "SUCCESS":
            print(result[1])
            sys.exit()

print(-1)