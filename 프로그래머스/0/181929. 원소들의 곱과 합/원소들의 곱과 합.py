def solution(num_list):
    answer = 0
    A = 1
    B = 0
    
    for num in num_list:
        A *= num
        B += num
    
    B = B ** 2
    
    if A > B:
        answer = 0
    else:
        answer = 1
        
    return answer