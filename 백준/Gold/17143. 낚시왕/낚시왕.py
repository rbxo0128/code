import sys

n, m, k = map(int, sys.stdin.readline().split())

sharks = {}
for i in range(k):
    x,y,s,d,z = map(int, sys.stdin.readline().split())
    sharks[(x-1,y-1)] = [s,d,z]

answer = 0

def move(sharks):
    new_sharks = {}
    for (x, y), (s, d, z) in sharks.items():
        nx, ny, nd = x, y, d

        if nd <= 2:
            cycle = (n - 1) * 2
            if cycle > 0:
                dist = s % cycle
                if nd == 1: pos = (cycle - x) + dist
                else: pos = x + dist
                pos_x = pos % cycle
                if pos_x >= n:
                    nx = cycle - pos_x
                    nd = 1
                else:
                    nx = pos_x
                    nd = 2
        else:
            cycle = (m - 1) * 2
            if cycle > 0:
                dist = s % cycle
                if nd == 4: pos = (cycle - y) + dist
                else: pos = y + dist
                pos_y = pos % cycle
                if pos_y >= m:
                    ny = cycle - pos_y
                    nd = 4
                else:
                    ny = pos_y
                    nd = 3

        if (nx, ny) in new_sharks:
            if new_sharks[(nx, ny)][2] < z:
                new_sharks[(nx, ny)] = [s, nd, z]
        else:
            new_sharks[(nx, ny)] = [s, nd, z]

    return new_sharks

def catch(i, sharks):
    global answer
    min_x = n
    temp = None
    for (x, y) in sharks:
        if y == i and x < min_x:
            min_x = x
            temp = (x, y)

    if temp:
        answer += sharks[temp][2]
        sharks.pop(temp)

    return sharks
    
for i in range(m):
    sharks = catch(i, sharks)
    sharks = move(sharks)

print(answer)