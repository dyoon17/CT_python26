def solution(myStr):
    answer = []
    new = ''
    
    if myStr.count('a') + myStr.count('b') + myStr.count('c') == len(myStr):
        answer = ["EMPTY"]
    else:       
        for s in myStr:
            if s == 'a' or s =='b' or s == 'c':
                new += ' '
            else:
                new += s
        
        answer = new.split()
                
    
    return answer