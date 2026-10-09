def solution(myString):
    answer = ''
    A = 'abcdefghijk'
    
    for i in myString:
        if i in A:
            answer += 'l'
        else:
            answer += i
    return answer