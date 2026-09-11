def solution(numbers):
    new = sorted(numbers)
        
    A = new[-1] * new[-2]
    B = new[0] * new[1]
        
    answer = max(A, B)
        
    return answer