def solution(myString):
    answer = ''
    
    for i in myString:
        if i.islower() == True:
            i = i.upper()
            answer += i
        else:
            answer += i
            
    return answer