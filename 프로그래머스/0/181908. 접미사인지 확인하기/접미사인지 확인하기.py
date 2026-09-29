def solution(my_string, is_suffix):
    answer = 0
    R = []
    
    for i in range(len(my_string)):
        R.append(my_string[-i:])
        
    if is_suffix in R:
        answer = 1
    else:
        answer = 0
    return answer