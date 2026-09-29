def solution(my_string, is_prefix):
    answer = 0
    R = []
    
    for i in range(len(my_string)):
        R.append(my_string[:i])
    
    if is_prefix in R:
        answer = 1
    
    return answer