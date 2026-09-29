def solution(my_string, s, e):
    answer = ''
    string = my_string[s:e+1]
    string = string[::-1]
    
    answer = my_string[:s] + string + my_string[e+1:]
    
    return answer