def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    
    if len(set(dice)) == 1:
        answer = a * 1111
        
    elif len(set(dice)) == 2:
        unique = list(set(dice))
        if dice.count(unique[0]) == 3:
            answer = (10 * unique[0] + unique[1]) ** 2
        elif dice.count(unique[0]) == 1:
            answer = (10 * unique[1] + unique[0]) ** 2
        else:
            answer = (unique[1] + unique[0]) * abs(unique[1] - unique[0])
        
    elif len(set(dice)) == 3:
        if a == b:
            answer = c * d
        elif a == c:
            answer = b * d
        elif a == d:
            answer = b * c
        elif b == c:
            answer = a * d
        elif b == d:
            answer = a * c
        elif c == d:
            answer = a * b
        
    else:
        answer = min(a, b, c, d)
            
    return answer