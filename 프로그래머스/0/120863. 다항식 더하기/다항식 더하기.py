def solution(polynomial):
    answer = ''
    X = 0
    P = 0
    new = polynomial.split()
    
    for x in new:
        if 'x' in x:
            if x == 'x':
                X += 1
            else:
                if len(x) == 2:
                    X += int(x[0])
                else:
                    X += (10*int(x[0]) + int(x[1]))
        elif '+' in x:
            continue
        else:
            if len(x) == 2:
                P += (10*int(x[0]) + int(x[1]))
            else:
                P += int(x[0])
                    
    if X > 1:
        answer += str(X)
        answer += "x"  
        if P > 0:            
            answer += " + "
            answer += str(P)
    elif X == 1:
        answer += 'x'
        if P > 0:            
            answer += " + "
            answer += str(P)
    else:
        if P > 0:                
            answer += str(P)   
        
    return answer