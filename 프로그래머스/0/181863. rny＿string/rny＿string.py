def solution(rny_string):
    answer = ''
    
    for str in rny_string:
        if str == 'm':
            answer += 'rn'
        else:
            answer += str
    return answer