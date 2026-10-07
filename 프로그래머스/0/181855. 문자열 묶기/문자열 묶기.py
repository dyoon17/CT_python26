def solution(strArr):
    answer = 0
    length = []
    
    for string in strArr:
        length.append(len(string))
    
    for i in range(1, 31):
        count = length.count(i)
        answer = max(answer, count)
        
    return answer