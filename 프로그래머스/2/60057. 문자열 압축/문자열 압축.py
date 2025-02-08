def solution(s):
    half = len(s)//2
    arr=[]
    answer = len(s)
    for j in range(1,half+1):
        count=1
        check=[]
        for i in range(0,len(s),j):
            if s[i:i+j] == s[i+j:i+j+j]:
                count+=1
            else:
                if count > 1:
                    check.append(str(count) + s[i:i+j])
                else:
                    check.append(s[i:i+j])
                count = 1
        check_str = ''.join(check)
        answer = min(answer, len(check_str))

    return answer