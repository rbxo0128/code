import sys
from collections import deque

t= int(sys.stdin.readline())

for i in range(t):
    opration = list(sys.stdin.readline().strip())

    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()
    arr = arr[1:-1]
    if n == 0:
        graph = []
    else:
        graph = deque(map(int,arr.split(",")))

    
    reverse = False
    isError = False
    for op in opration:
        if op == "R":
            reverse = not reverse

        if op == "D":
            if graph:
                if reverse:
                    graph.pop()
                else:
                    graph.popleft()
            
            else:
                print("error")
                isError = True
                break

    if isError:
        continue

    if reverse:
        graph.reverse()
        print("["+ ','.join(map(str,graph)) +"]")

    else:
        print("["+ ','.join(map(str,graph)) +"]")