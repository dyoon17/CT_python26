def solution(a, b):
    answer = 0
    
    if a % 2 == 1:
        if b % 2 == 1:
            answer = a ** 2 + b ** 2
        else:
            answer = 2 * (a + b)
    else:
        if b % 2 == 1:
            answer = 2 * (a + b)
        else:
            answer = abs(a - b)
            
    return answer