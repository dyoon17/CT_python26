def solution(myString, pat):
    answer = 0
    new_pat = ''
    
    for a in pat:
        if a == 'A':
            new_pat += 'B'
        else:
            new_pat += 'A'
    
    for i in range(len(myString)):
        if myString[i:i+len(new_pat)] == new_pat:
            answer = 1
            break
            
    return answer