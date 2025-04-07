import sys

n,m = map(int,sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

count = 0

def DFS(total, idx):
    global count
    if total == m:
        count+=1

    for i in range(idx+1,n):
        DFS(total+arr[i],i)



for i in range(n):
    DFS(arr[i],i)


print(count)