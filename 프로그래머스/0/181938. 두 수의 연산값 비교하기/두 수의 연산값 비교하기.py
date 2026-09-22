def solution(a, b):
    answer = 0
    a_b = str(a) + str(b)
    mul = 2 * a * b
    
    if int(a_b) >= mul:
        answer = int(a_b)
    else:
        answer = mul
    return answer