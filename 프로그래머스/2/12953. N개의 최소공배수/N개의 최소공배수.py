import math

def solution(arr):
    while len(arr) != 2:
        x,y = arr.pop(), arr.pop()
        arr.append(x*y//math.gcd(x,y))
        
    return arr[0]*arr[1]//math.gcd(arr[0],arr[1])

