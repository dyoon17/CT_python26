def solution(myString):
    answer = []
    
    myString = myString.split('x')
    myString = sorted(myString)
    
    for string in myString:
        if string != "":
            answer.append(string)
    return answer