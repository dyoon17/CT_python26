def solution(arr):
    answer = []
    
    for arr_2 in arr:
        new = []
        for i in arr_2:
            if len(arr) > len(arr_2):
                for _ in range(len(arr) - len(arr_2)):
                    arr_2.append(0)
            elif len(arr) < len(arr_2):
                for _ in range(len(arr_2)):
                    new.append(0)
                for _ in range(len(arr_2) - len(arr)):
                    arr.append(new)
    return arr