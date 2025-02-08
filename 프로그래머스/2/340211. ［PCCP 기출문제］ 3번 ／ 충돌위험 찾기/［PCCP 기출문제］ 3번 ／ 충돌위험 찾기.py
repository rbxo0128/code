def solution(points, routes):
    time = [{}]
    
    for i in routes:
        times=0
        for j in range(len(i)-1):
            x1, y1 = points[i[j]-1]
            x2, y2 = points[i[j+1]-1]
            
            if times == 0:
                cur_pos = [x1,y1]
                if not time[times].get(str(cur_pos)):
                    time[times][str(cur_pos)] = 1
                else:
                    time[times][str(cur_pos)] += 1
                
            while cur_pos[0] != x2:
                if cur_pos[0] < x2:
                    cur_pos[0] += 1
                else:
                    cur_pos[0] -= 1
                    
                times+=1
                if(times >= len(time)):
                    time.append({})
                
                if not time[times].get(str(cur_pos)):
                    time[times][str(cur_pos)] = 1
                else:
                    time[times][str(cur_pos)] += 1
                    
            while cur_pos[1] != y2:
                if cur_pos[1] < y2:
                    cur_pos[1] += 1
                else:
                    cur_pos[1] -= 1
                times+=1
                if(times >= len(time)):
                    time.append({})
                if not time[times].get(str(cur_pos)):
                    time[times][str(cur_pos)] = 1
                else:
                    time[times][str(cur_pos)] += 1
    
    count=0
    for i in time:
        count += sum(value >= 2 for value in i.values())
    
    answer = count
    return answer