def solution(intStrs, k, s, l):
    answer = []
    new = []
    num = ''
    
    for string in intStrs:        
        new.append(string[s:s+l])        
        
    for n in new:
        if int(n) > k:
            answer.append(int(n))
            
    return answer