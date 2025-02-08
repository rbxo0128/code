def solution(friends, gifts):
    
    friend_dict = [[0] * len(friends) for i in range(len(friends))]
    a,b=0,0
    for i in gifts:
        from_f , to = i.split()
        for j in range(len(friends)):
            if from_f == friends[j]:
                a = j
            if to == friends[j]:
                b = j
        friend_dict[a][b] += 1
    
    list_dict = [0 for i in range(len(friends))]

    for i in range(len(friends)):
        for j in friend_dict[i]:
            list_dict[i] += j
        for k in range(len(friends)):
            list_dict[i] -= friend_dict[k][i]
    
    present = [0 for i in range(len(friends))]
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j:
                break
            else:
                if friend_dict[i][j] > friend_dict[j][i]:
                    present[i] +=1
                elif friend_dict[i][j] < friend_dict[j][i]:
                    present[j] +=1
                else:
                    if (list_dict[i] > list_dict[j]):
                        present[i]+=1
                    elif(list_dict[i] < list_dict[j]):
                        present[j]+=1
                    else:
                        pass
    print(max(present))
    answer = 0
    return max(present)