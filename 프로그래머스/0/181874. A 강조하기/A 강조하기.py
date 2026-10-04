def solution(myString):
    answer = ''
    
    for i in myString:
        if i == 'a':
            answer += 'A'
        elif i != 'A':
            i = i.lower()
            answer += i
        else:
            answer += i
    return answer