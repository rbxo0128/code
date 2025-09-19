import sys
input = sys.stdin.readline

n = input().strip()

ducks = [0]

for i in range(len(n)):
    check = False
    if n[i] == "q":
        for j in range(len(ducks)):
            if ducks[j] % 5 == 0:
                ducks[j] += 1
                check = True
                break
        if not check:
            ducks.append(1)
            continue
 
    elif n[i] == "u":
        for j in range(len(ducks)):
            if ducks[j] % 5 == 1:
                ducks[j] += 1
                check = True
                break

    elif n[i] == "a":
        for j in range(len(ducks)):
            if ducks[j] % 5 == 2:
                ducks[j] += 1
                check = True
                break

    elif n[i] == "c":
        for j in range(len(ducks)):
            if ducks[j] % 5 == 3:
                ducks[j] += 1
                check = True
                break

    elif n[i] == "k":
        for j in range(len(ducks)):
            if ducks[j] % 5 == 4:
                ducks[j] += 1
                check = True
                break

    if not check:
        print(-1)
        exit()

if all(d % 5 == 0 for d in ducks):
    print(len(ducks))
else:
    print(-1)