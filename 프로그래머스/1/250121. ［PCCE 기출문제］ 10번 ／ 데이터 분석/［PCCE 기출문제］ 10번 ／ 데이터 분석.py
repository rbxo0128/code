def solution(data, ext, val_ext, sort_by):
    ext_list = ["code","date","maximum","remain"]
    ext_idx = ext_list.index(ext)
    data.sort(key = lambda x:x[ext_idx])
    
    idx = -1
    for i in range(len(data)):
        if val_ext <= data[i][ext_idx]:
            idx = i
            break
    sort_idx = ext_list.index(sort_by)
    answer = sorted(data[:idx], key = lambda x:x[sort_idx])
    
    return answer