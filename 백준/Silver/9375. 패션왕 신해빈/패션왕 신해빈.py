import sys

n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    clothes = []
    for i in range(m):
        clothes.append(list(sys.stdin.readline().split()))



    cloth = {}
    for x,y in clothes:
        if y in cloth:
            cloth[y].append(x)
        else:
            cloth[y] = [x]
    if len(cloth) == 1:
        for i in cloth:
            print(len(cloth[i]))
    else:
        answer = 1
        for i in cloth:
            answer *= len(cloth[i])+1
                
        print(answer-1)