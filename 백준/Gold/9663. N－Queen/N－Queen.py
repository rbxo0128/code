import sys

n= int(sys.stdin.readline())

def DFS(x, y, cross1, cross2):
    if x == n:
        return 1

    count = 0
    for col in range(n):
        if col in y or (x - col) in cross1 or (x + col) in cross2:
            continue
        
        count += DFS(x + 1, y | {col}, cross1 | {x-col}, cross2 | {x+col})
    
    return count
y = set()
cross1 = set()
cross2 = set()
print(DFS(0, y, cross1, cross2))