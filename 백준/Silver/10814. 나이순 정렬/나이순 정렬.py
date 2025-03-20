import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    arr.append([age,name])

arr_sort = sorted(arr, key= lambda x: x[0])

for x,y in arr_sort:
    print(x,y)