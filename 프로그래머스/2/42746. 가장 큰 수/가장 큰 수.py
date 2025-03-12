def solution(numbers):
    
    numbers = list(map(str,numbers))
    
    numbers.sort(key=lambda x: x * 10, reverse=True)
    
    a = ''.join(numbers)
    if int(a) == 0:
        return "0"

    return a