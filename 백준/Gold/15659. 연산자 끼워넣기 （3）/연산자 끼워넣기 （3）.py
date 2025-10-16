import sys

def func(i, ops, plus, minus, mul, div, arr):
    global minresult, maxresult, a

    if i == a:
        result = ''.join(str(n) + o for n, o in zip(arr, ops)) + str(arr[-1])
        result = eval(result)
        minresult = min(minresult, result)
        maxresult = max(maxresult, result)
        return


    if plus > 0:
        ops.append("+")
        func(i+1, ops, plus-1, minus, mul, div,arr)
        ops.pop()

    if minus>0:
        ops.append("-")
        func(i+1, ops, plus, minus-1, mul, div,arr)
        ops.pop()
    
    if mul > 0:
        ops.append("*")
        func(i+1, ops, plus, minus, mul-1, div,arr)
        ops.pop()
    
    if div > 0:
        ops.append("//")
        func(i+1, ops, plus, minus, mul, div-1,arr)
        ops.pop()


a = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
plus,minus,mul,div = map(int,sys.stdin.readline().split())

minresult = float("inf")
maxresult = -float("inf")

func(1,[],plus,minus,mul,div, arr)

print(maxresult)
print(minresult)