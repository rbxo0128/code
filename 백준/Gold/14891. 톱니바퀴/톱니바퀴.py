import sys
from collections import deque

def rotate(wheel, direction):
    if direction == -1:
        wheel.append(wheel.popleft())
    elif direction == 1:
        wheel.appendleft(wheel.pop())

# 바퀴 입력
wheel_list = [deque(map(int, sys.stdin.readline().strip())) for _ in range(4)]

# 회전 연산 입력
k = int(sys.stdin.readline())
operations = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

for num, direction in operations:
    num -= 1  # 0-based 인덱스로 변환
    rotate_dirs = [0] * 4
    rotate_dirs[num] = direction

    # 왼쪽 확인
    for i in range(num - 1, -1, -1):
        if wheel_list[i][2] != wheel_list[i + 1][6]:
            rotate_dirs[i] = -rotate_dirs[i + 1]
        else:
            break

    # 오른쪽 확인
    for i in range(num + 1, 4):
        if wheel_list[i - 1][2] != wheel_list[i][6]:
            rotate_dirs[i] = -rotate_dirs[i - 1]
        else:
            break

    # 회전 적용
    for i in range(4):
        if rotate_dirs[i]:
            rotate(wheel_list[i], rotate_dirs[i])

# 점수 계산
result = 0
for i in range(4):
    if wheel_list[i][0] == 1:
        result += (1 << i)

print(result)