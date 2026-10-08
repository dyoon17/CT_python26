def solution(my_string, target):
    answer = 0
    
    for i in range(len(my_string)):
        if my_string[i:i+len(target)] == target:
            answer = 1
            
    return answer