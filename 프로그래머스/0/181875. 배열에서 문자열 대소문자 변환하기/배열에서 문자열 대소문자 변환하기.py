def solution(strArr):
    answer = []
    
    for i in range(len(strArr)):
        if i % 2 == 0:
            strArr[i] = strArr[i].lower()
            answer.append(strArr[i])
        else:
            strArr[i] = strArr[i].upper()
            answer.append(strArr[i])
    return answer