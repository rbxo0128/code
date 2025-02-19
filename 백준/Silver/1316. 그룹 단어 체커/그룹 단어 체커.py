import sys

n = int(sys.stdin.readline())

count = 0
for i in range(n):
    a = sys.stdin.readline().strip()
    stack1 = set()
    stack = []

    for j in range(len(a)):
        if not (a[j] in stack1):
            if stack:
                stack.pop()
            stack1.add(a[j])
            stack.append(a[j])
        else:
            if stack.pop() == a[j]:
                stack.append(a[j])
            else:
                count+=1
                break

print(n-count)