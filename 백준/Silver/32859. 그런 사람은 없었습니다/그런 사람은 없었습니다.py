n,m = map(int, input().split())
s = int(input())
c = [0 for i in range(n)]
arr = [] # 폼
arr2 = [] # 돈
answer = set()
for i in range(m):
    x,y = map(int,input().split())
    if y == 0:
        arr.append(x)
        if x in arr2:
            arr2.remove(x)
            
        for j in arr2:
            c[j-1] += 1
            if c[j-1]>=s:
                answer.add(j)

    elif y == 1:
        if not x in arr:
            arr2.append(x)        
    
if answer:
    for i in sorted(answer):
        print(i)
else:
    print(-1)