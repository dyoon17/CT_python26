def solution(s):
    answer = True
    count = 0
        
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            answer = False
    
    if count > 0:
        answer = False

    return answer