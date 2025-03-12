import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    name, kor, eng, math = sys.stdin.readline().split()
    arr.append([name, int(kor), int(eng), int(math)])

arr = sorted(arr, key=lambda x: (-x[1],x[2],-x[3], x[0]))
for name,kor,eng,math in arr:
    print(name)