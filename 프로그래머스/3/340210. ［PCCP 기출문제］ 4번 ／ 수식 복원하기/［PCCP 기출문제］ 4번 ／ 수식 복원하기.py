from collections import Counter

def solution(expressions):
    answer_list = []
    answer_check = []
    true_decimal = []
    decimal = set()
    for i in expressions:
        if i[-1]=="X":
            answer_check.append(i)
        else:
            answer_list.append(i)
        
        for j in range(len(i)):
            if i[j].isdigit():
                decimal.add(i[j])
    answer_lists = []
    answer_checks= []
    data_check = [[] for i in range(len(answer_check))]
    for i in range(len(answer_list)):
        answer_lists.append(answer_list[i].split())
    for i in range(len(answer_check)):
        answer_checks.append(answer_check[i].split())
    
    for m in range(int(max(decimal))+1,10):
        for i in range(len(answer_lists)):
            data = [int(answer_lists[i][0]),int(answer_lists[i][2]),int(answer_lists[i][4])]
            for j in range(len(answer_lists[i])):
                sum=0
                a = len(answer_lists[i][j])
                if a >= 2:
                    start = a-1
                    for k in range(a):
                        sum += int(answer_lists[i][j][k:k+1])*m**start
                        start-=1
                    data[int(j/2)] = sum

            if (answer_lists[i][1] == '+'):
                if(data[0] + data[1] == data[2]):
                    true_decimal.append(m)
            else:
                if(data[0] - data[1] == data[2]):
                    true_decimal.append(m)
    
    counter = Counter(true_decimal)
    
    true_decimals = [num for num, count in counter.items() if count == len(answer_list)]
    if max(decimal) == '8':
        true_decimals.append(9)
        
    for m in set(true_decimals):
        print("decimal = " + str(m))
        for i in range(len(answer_checks)):
            data = [int(answer_checks[i][0]),int(answer_checks[i][2])]
            for j in range(len(answer_checks[i])):
                sum=0
                a = len(answer_checks[i][j])
                if a >= 2:
                    start = a-1
                    for k in range(a):
                        sum += int(answer_checks[i][j][k:k+1])*m**start
                        start-=1
                    data[int(j/2)] = sum

            if (answer_checks[i][1] == '+'):
                data_check[i].append(str(decimals(data[0]+data[1],m)))
            else:
                data_check[i].append(str(decimals(data[0]-data[1],m)))
    
    if len(true_decimals) == 0:
        for i in range(len(answer_checks)):
            data = [int(answer_checks[i][0]),int(answer_checks[i][2])]
            for m in range(int(max(decimal))+1,10):
                for j in range(len(answer_checks[i])):
                    sum=0
                    a = len(answer_checks[i][j])
                    if a >= 2:
                        start = a-1
                        for k in range(a):
                            sum += int(answer_checks[i][j][k:k+1])*m**start
                            start-=1
                        data[int(j/2)] = sum
                if answer_checks[i][1] == '+':
                    data_check[i].append(str(decimals(data[0]+data[1],m)))
                elif answer_checks[i][1] == '-':
                    data_check[i].append(str(decimals(data[0]-data[1],m)))
    print(data_check)

    for i in range(len(data_check)):
        if len(set(data_check[i])) == 1:
            answer_checks[i][4] = str(data_check[i][0])
        else:
            answer_checks[i][4] = '?'
    
    print(answer_checks)
    result = [' '.join(sublist) for sublist in answer_checks]

    return result

def decimals(n, base):
    if n== 0:
        return 0
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    
    return ''.join(str(x) for x in digits[::-1])