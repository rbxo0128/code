import sys
import math
from collections import deque

input = sys.stdin.readline

n = int(input())

op = list(input().split())

def DFS(level, result, is_max):
    if level == n+1:
        print("".join(map(str,result)))
        return True

    if is_max:
        num = range(9, -1, -1)
    else:
        num = range(10)
    
    for i in num:
        if i not in result:
            if level == 0 or (op[level-1] == ">" and result[-1] > i) or (op[level-1] == "<" and result[-1] < i):
                result.append(i)
                if DFS(level+1, result, is_max):
                    return True
                result.pop()
    return False

DFS(0, [], True)
DFS(0, [], False)