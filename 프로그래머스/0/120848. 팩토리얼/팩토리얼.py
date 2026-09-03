def solution(n):
    max = 0
    factorial = 1
    
    for i in range(1, n+1):
        factorial *= i
        if n >= factorial:
            max += 1
        else:
            break
    return max