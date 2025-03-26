def solution(n, arr1, arr2):
    result = []
    for i in range(len(arr1)):
        arr1_bi = bin(arr1[i])[2:].zfill(n)
        arr2_bi = bin(arr2[i])[2:].zfill(n)
        
        decode = []
        for j in range(n):
            if arr1_bi[j] == "1" or arr2_bi[j] == "1":
                decode.append("#")
                continue
                
            decode.append(" ")

        result.append(''.join(decode))
        
    return result