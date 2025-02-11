def solution(schedules, timelogs, startday):
    arr = []
    
    for time in schedules:
        i = str(time)
        if time<1000:
            hour = i[0:1]
            minute = i[1:]
        else:
            hour = i[0:2]
            minute = i[2:]
        minute = int(minute) + 10
        if minute >= 60:
            minute -= 60
            hour = int(hour) + 1
            
        arr.append(int(hour)*60+int(minute))
    
    user_id = 0
    count = 0
    for user in timelogs:
        day = startday
        for time in user:
            if not (day%7 ==6 or day%7==0):
                i = str(time)
                if time<1000:
                    hour = i[0:1]
                    minute = i[1:]
                else:
                    hour = i[0:2]
                    minute = i[2:]

                x = int(hour)*60+int(minute)
                if arr[user_id] < x:
                    print(arr[user_id],x)
                    print(time)
                    count+=1
                    break
            day += 1
        user_id+=1
    print(arr)
        
    return len(schedules)-count