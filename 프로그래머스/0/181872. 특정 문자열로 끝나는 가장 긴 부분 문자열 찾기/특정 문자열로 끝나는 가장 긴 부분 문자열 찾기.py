def solution(myString, pat):
    answer = ''
    
    for i in range(len(myString)-1, -1, -1):
        if myString[i] == pat[-1]:
            answer = myString[:i+1]
            break    
    return answer