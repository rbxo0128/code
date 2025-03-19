import sys

n,d,k,c = map(int, sys.stdin.readline().split())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

sushi_dict = {}
for i in range(k):
    if arr[i] in sushi_dict:
        sushi_dict[arr[i]]+=1
    else:
        sushi_dict[arr[i]] = 1
    arr.append(arr[i])



left = 0
right = k-1
maxs = len(sushi_dict)
if not c in sushi_dict:
    maxs+=1

while right < n+k-1:
    sushi_dict[arr[left]] -= 1
    if sushi_dict[arr[left]] == 0:
        del sushi_dict[arr[left]]

    left+=1
    right+=1

    if arr[right] in sushi_dict:
        sushi_dict[arr[right]] +=1
    else:
        sushi_dict[arr[right]] = 1
 
    length = len(sushi_dict)
    if not c in sushi_dict:
        length+=1

    maxs = max(length,maxs)

    
print(maxs)