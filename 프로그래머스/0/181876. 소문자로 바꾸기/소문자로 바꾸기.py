def solution(myString):
    answer = ''
    
    for i in myString:
        if i.isupper() == True:
            i = i.lower()
            answer += i
        else:
            answer += i
    return answer