import sys
import math
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

b,c = map(int,input().split())
answer = 0

answer += len(arr)
for num in arr:
    if num - b > 0:
        answer += math.ceil((num - b) / c)
        
print(answer)