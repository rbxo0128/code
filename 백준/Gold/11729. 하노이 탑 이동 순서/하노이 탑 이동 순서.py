import sys

def hanoi(n, start, mid, to, result):
    if n == 1:
        result.append([start,to])
        return

    hanoi(n-1,start,to,mid, result)
    result.append([start,to])
    hanoi(n-1, mid, start, to, result)


n = int(sys.stdin.readline())

result = []
hanoi(n,1,2,3,result)

print(len(result))
for x,y in result:
    print(x,y)