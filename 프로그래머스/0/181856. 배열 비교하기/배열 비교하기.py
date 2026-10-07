def solution(arr1, arr2):
    answer = 0
    sum_1 = 0
    sum_2 = 0
    
    if len(arr1) != len(arr2):
        if len(arr1) < len(arr2):
            answer = -1
        else:
            answer = 1
    else:
        for i in range(len(arr1)):
            sum_1 += arr1[i]
        
        for i in range(len(arr2)):
            sum_2 += arr2[i]
            
        if sum_1 > sum_2:
            answer = 1
        elif sum_1 < sum_2:
            answer = -1
        else:
            answer = 0           
        
    return answer