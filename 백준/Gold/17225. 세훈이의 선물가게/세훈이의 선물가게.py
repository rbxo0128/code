import sys

input = sys.stdin.readline

b,r,n = map(int, input().split())

time = [b,r]
arr = []
temp = [0,0]
for i in range(n):
    t, color, num = input().split()
    t = int(t)
    num = int(num)

    color = 0 if color == "B" else 1

    t = max(temp[color], t)

    for j in range(num):
        arr.append((t+j*time[color], color))

    temp[color] = t+num*time[color]

result = [[],[]]
arr.sort()
for i in range(1, len(arr)+1):
    result[arr[i-1][1]].append(i)

print(len(result[0]))
print(" ".join(map(str, result[0])))
print(len(result[1]))
print(" ".join(map(str, result[1])))