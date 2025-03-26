def solution(dartResult):
    left=0
    result = []
    for right in range(len(dartResult)):
        if dartResult[right] == "S":
            
            num = dartResult[left:right]
            left = right+1
            if num.isdigit():
                result.append(int(num))
            else:
                if num[0] == "*":
                    if len(result) <= 1:
                        result[0] *= 2
                    else:
                        result[-1] *= 2
                        result[-2] *= 2
                    
                elif num[0] == "#":
                    result[-1] = -result[-1]

                result.append(int(num[1:]))
            
            
        elif dartResult[right] == "D":
            num = dartResult[left:right]
            left = right+1

            if num.isdigit():
                result.append(int(num)**2)
            else:
                if num[0] == "*":
                    if len(result) <= 1:
                        result[0] *= 2
                    else:
                        result[-1] *= 2
                        result[-2] *= 2
                    
                elif num[0] == "#":
                    result[-1] = -result[-1]

                result.append(int(num[1:])**2)
            
            
        elif dartResult[right] == "T":
            num = dartResult[left:right]
            left = right+1

            if num.isdigit():
                result.append(int(num)**3)
            else:
                if num[0] == "*":
                    if len(result) <= 1:
                        result[0] *= 2
                    else:
                        result[-1] *= 2
                        result[-2] *= 2
                    
                elif num[0] == "#":
                    result[-1] = -result[-1]

                result.append(int(num[1:])**3)
            
    if dartResult[-1] == "*":
        result[-1] *= 2
        result[-2] *= 2
    elif dartResult[-1] == "#":
        result[-1] = -result[-1]
        
    #코드에 문제가 많음
    return sum(result)