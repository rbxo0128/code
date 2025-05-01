import sys

n = sys.stdin.readline().strip()

arr = set()
for i in n:
    if i.isdigit():
        arr.add(i)
        
print(len(arr))