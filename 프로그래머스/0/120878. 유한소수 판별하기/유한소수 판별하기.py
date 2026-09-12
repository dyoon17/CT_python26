def solution(a, b):
    answer = 0
    gcd = 1
    
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            gcd = i
        else:
            continue
    
    den = b // gcd
    
    while den % 2 == 0:
        den //= 2
    while den % 5 == 0:
        den //= 5
    
    if den == 1:
        return 1
    else:
        return 2