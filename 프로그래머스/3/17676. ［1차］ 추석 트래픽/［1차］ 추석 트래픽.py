def solution(lines):
    times = []
    for line in lines:
        h = int(line[11:13])
        m = int(line[14:16])
        s = int(line[17:19])
        ms = int(line[20:23])
        
        end_time = (h * 60 * 60 + m * 60 + s) * 1000 + ms
        t = int(float(line[24:-1]) * 1000)
        start_time = end_time - t + 1
        
        times.append([start_time, end_time])

    max_count = 0

    for i in range(len(times)):
        point1 = times[i][0]
        count1 = 0
        for j in range(len(times)):
            if times[j][0] <= point1 + 999 and times[j][1] >= point1:
                count1 += 1

        point2 = times[i][1]
        count2 = 0
        for j in range(len(times)):
            if times[j][0] <= point2 + 999 and times[j][1] >= point2:
                count2 += 1

        max_count = max(max_count, count1, count2)

    return max_count