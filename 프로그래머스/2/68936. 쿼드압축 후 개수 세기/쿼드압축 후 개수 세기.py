def solution(arr):
    def DFS(arr):
        x,y = 0,0
        total = sum(sum(x) for x in arr)
        if total == 0:
            return [1, 0]
        if total == len(arr) ** 2:
            return [0, 1]
        
        n = len(arr) // 2
        arr1 = [x[:n] for x in arr[:n]]
        a,b = DFS(arr1)
        x += a
        y += b
        arr2 = [x[n:] for x in arr[:n]]
        a,b = DFS(arr2)
        x += a
        y += b
        arr3 = [x[:n] for x in arr[n:]]
        a,b = DFS(arr3)
        x += a
        y += b
        arr4 = [x[n:] for x in arr[n:]]
        a,b = DFS(arr4)
        x += a
        y += b

        return [x,y]
    return DFS(arr)