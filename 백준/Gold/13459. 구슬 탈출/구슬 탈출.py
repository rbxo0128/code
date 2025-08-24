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

stack = deque([(red, blue, 0)])
visited = set()
visited.add((red[0], red[1], blue[0], blue[1]))
cnt = 0

while stack:
    r, b, cnt = stack.popleft()
    cnt += 1
    if cnt > 10:
        break

    rx, ry = r[0], r[1]
    bx, by = b[0], b[1]

    # Left 이동
    i = 1
    withBlue = False
    bluehole = False 
    redhole = False
    while True:
        if rx == bx and ry - i == by:
            withBlue = True
        if graph[rx][ry - i] == ".":
            i += 1
        elif graph[rx][ry - i] == "O":
            redhole = True
            left_red = (rx, ry - i)
            break
        elif graph[rx][ry - i] == "#":
            left_red = (rx, ry - i + 1)
            break

    if withBlue:
        bluehole=True
        if not redhole:
            left_blue = left_red
            left_red = (left_red[0], left_red[1] + 1)
            if not (left_red[0], left_red[1], left_blue[0], left_blue[1]) in visited:
                visited.add((left_red[0], left_red[1], left_blue[0], left_blue[1]))
                stack.append((left_red, left_blue, cnt))
    else:
        i = 1
        while True:
            if graph[bx][by - i] == ".":
                i += 1
            elif graph[bx][by - i] == "O":
                bluehole = True
                break
            elif graph[bx][by - i] == "#":
                left_blue = (bx, by - i + 1)
                break
        if redhole and not bluehole:
            break
        
        if not bluehole:
            if left_red[0] == left_blue[0] and left_red[1] == left_blue[1]:
                left_blue = (left_blue[0], left_blue[1] + 1)

            if not (left_red[0], left_red[1], left_blue[0], left_blue[1]) in visited:
                visited.add((left_red[0], left_red[1], left_blue[0], left_blue[1]))
                stack.append((left_red, left_blue, cnt))

    # Right 이동
    i = 1
    bluehole = False
    withBlue = False
    redhole = False
   
    while True:
        if rx == bx and ry + i == by:
            withBlue = True
        if graph[rx][ry + i] == ".":
            i += 1
        elif graph[rx][ry + i] == "O":
            redhole = True
            right_red = (rx, ry + i)
            break
        elif graph[rx][ry + i] == "#":
            right_red = (rx, ry + i - 1)
            break

    if withBlue:
        bluehole=True
        if not redhole:
            right_blue = right_red
            right_red = (right_red[0], right_red[1] - 1)
            if not (right_red[0], right_red[1], right_blue[0], right_blue[1]) in visited:
                visited.add((right_red[0], right_red[1], right_blue[0], right_blue[1]))
                stack.append((right_red, right_blue, cnt))
    else:
        i = 1
        while True:
            if graph[bx][by + i] == ".":
                i += 1
            elif graph[bx][by + i] == "O":
                bluehole = True
                break
            elif graph[bx][by + i] == "#":
                right_blue = (bx, by + i - 1)
                break
        if redhole and not bluehole:
            break
        if not bluehole:
            if right_red[0] == right_blue[0] and right_red[1] == right_blue[1]:
                right_blue = (right_blue[0], right_blue[1] - 1)
            if not (right_red[0], right_red[1], right_blue[0], right_blue[1]) in visited:
                visited.add((right_red[0], right_red[1], right_blue[0], right_blue[1]))
                stack.append((right_red, right_blue, cnt))

    # Up 이동
    i = 1
    bluehole = False
    withBlue = False
    redhole = False
    while True:
        if rx - i == bx and ry == by:
            withBlue = True
        if graph[rx - i][ry] == ".":
            i += 1
        elif graph[rx - i][ry] == "O":
            redhole = True
            up_red = (rx - i, ry)
            break
        elif graph[rx - i][ry] == "#":
            up_red = (rx - i + 1, ry)
            break

    if withBlue:
        bluehole=True
        if not redhole:
            up_blue = up_red
            up_red = (up_red[0] + 1, up_red[1])
            if not (up_red[0], up_red[1], up_blue[0], up_blue[1]) in visited:
                visited.add((up_red[0], up_red[1], up_blue[0], up_blue[1]))
                stack.append((up_red, up_blue, cnt))
    else:
        i = 1
        while True:
            if graph[bx - i][by] == ".":
                i += 1
            elif graph[bx - i][by] == "O":
                bluehole = True
                break
            elif graph[bx - i][by] == "#":
                up_blue = (bx - i + 1, by)
                break
        if redhole and not bluehole:
            break
        if not bluehole:
            if up_red[0] == up_blue[0] and up_red[1] == up_blue[1]:
                up_blue = (up_blue[0] + 1, up_blue[1])
            if not (up_red[0], up_red[1], up_blue[0], up_blue[1]) in visited:
                visited.add((up_red[0], up_red[1], up_blue[0], up_blue[1]))
                stack.append((up_red, up_blue, cnt))

    # Down 이동
    i = 1
    bluehole = False
    withBlue = False
    redhole = False
    while True:
        if rx + i == bx and ry == by:
            withBlue = True
        if graph[rx + i][ry] == ".":
            i += 1
        elif graph[rx + i][ry] == "O":
            redhole = True
            down_red = (rx + i, ry)
            break
        elif graph[rx + i][ry] == "#":
            down_red = (rx + i - 1, ry)
            break

    if withBlue:
        bluehole=True
        if not redhole:
            down_blue = down_red
            down_red = (down_red[0] - 1, down_red[1])
            if not (down_red[0], down_red[1], down_blue[0], down_blue[1]) in visited:
                visited.add((down_red[0], down_red[1], down_blue[0], down_blue[1]))
                stack.append((down_red, down_blue, cnt))
    else:
        i = 1
        while True:
            if graph[bx + i][by] == ".":
                i += 1
            elif graph[bx + i][by] == "O":
                bluehole = True
                break
            elif graph[bx + i][by] == "#":
                down_blue = (bx + i - 1, by)
                break
        if redhole and not bluehole:
            break
        if not bluehole:
            if down_red[0] == down_blue[0] and down_red[1] == down_blue[1]:
                down_blue = (down_blue[0] - 1, down_blue[1])
            if not (down_red[0], down_red[1], down_blue[0], down_blue[1]) in visited:
                visited.add((down_red[0], down_red[1], down_blue[0], down_blue[1]))
                stack.append((down_red, down_blue, cnt))


if redhole:
    if bluehole:
        print(0)
    else:
        print(1)
else:
    print(0)
