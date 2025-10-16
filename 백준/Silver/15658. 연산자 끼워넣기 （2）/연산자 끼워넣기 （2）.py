import sys

def func(i, cur, plus, minus, mul, div, arr):
    global minresult, maxresult, a

    if i == a:
        minresult = min(minresult, cur)
        maxresult = max(maxresult, cur)
        return


    if plus > 0:
        func(i+1, cur + arr[i], plus-1, minus, mul, div,arr)

    if minus>0:
        func(i+1, cur - arr[i], plus, minus-1, mul, div,arr)
    
    if mul > 0:
        func(i+1, cur * arr[i], plus, minus, mul-1, div,arr)
    
    if div > 0:
        if cur >= 0:
            func(i+1, cur // arr[i], plus, minus, mul, div-1,arr)
        else:
            func(i+1, -(-cur // arr[i]), plus, minus, mul, div-1,arr)


a = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
plus,minus,mul,div = map(int,sys.stdin.readline().split())

minresult = float("inf")
maxresult = -float("inf")

func(1,arr[0],plus,minus,mul,div, arr)

print(maxresult)
print(minresult)