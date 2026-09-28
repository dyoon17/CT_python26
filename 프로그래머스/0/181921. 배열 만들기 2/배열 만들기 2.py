def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        if set(str(i)) == {'0', '5'}:
            answer.append(i)
        elif set(str(i)) == {'5'}:
            answer.append(i)
    
    if answer == []:
        answer = [-1]
    
    return answer