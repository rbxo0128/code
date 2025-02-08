def solution(video_len, pos, op_start, op_end, commands):
    video_len_min, video_len_sec = map(int,video_len.split(":"))
    video_len_total = video_len_min * 60 + video_len_sec
    
    pos_min, pos_sec = map(int, pos.split(":"))
    pos_total = pos_min*60 + pos_sec
    
    op_start_min, op_start_sec = map(int, op_start.split(":"))
    op_start_total = op_start_min*60+op_start_sec
    
    op_end_min, op_end_sec = map(int, op_end.split(":"))
    op_end_total = op_end_min*60+op_end_sec
    
    pos_total = op_check(pos_total,op_start_total,op_end_total)
    for i in commands:
        if i == "prev":
            pos_total-=10
            if(pos_total<0):
                pos_total = 0
            
        elif i == "next":
            pos_total+=10
            if(pos_total > video_len_total):
                pos_total = video_len_total
        
        pos_total = op_check(pos_total,op_start_total,op_end_total)
        
    answer = f'{pos_total//60:02}:{pos_total%60:02}'
    return answer


def op_check(pos_total,op_start_total,op_end_total):
    if(pos_total >= op_start_total and pos_total < op_end_total):
        return op_end_total
    else:
        return pos_total