def solution(arr):
    answer = []
    two = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            two.append(i)
    
    if 2 not in arr:
        answer = [-1]
    
    for i in range(len(two)):
        answer = arr[two[0]:two[-1]+1]
        
    
    return answer