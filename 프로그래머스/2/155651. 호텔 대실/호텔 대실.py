def solution(book_time):
    book = []
    for x,y in book_time:
        start = int(x[:2])*60 + int(x[3:])
        end = int(y[:2])*60 + int(y[3:])
        book.append([start,1])
        book.append([end+10,-1])
    
    book.sort()
    tmp = 0
    answer = 0
    for time,op in book:
        tmp += op
        answer = max(answer,tmp)
        
    return answer