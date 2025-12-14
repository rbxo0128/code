import sys

n = int(sys.stdin.readline())

count = 0
for num in range(1,n+1):
    if num < 100:
        count +=1
    
    elif num == 1000:
        pass

    else:
        str_num = str(num)
        if int(str_num[2]) - int(str_num[1]) == int(str_num[1]) - int(str_num[0]):
            count+=1

print(count)
