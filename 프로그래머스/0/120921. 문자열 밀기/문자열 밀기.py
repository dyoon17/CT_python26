def solution(A, B):
    answer = 0
    count = 0
    
    if A == B:
        answer = 0
        
    while A != B and count < len(A):
        A = A[-1] + A[0:-1]
        answer += 1
        count += 1
    
    if A != B:
        answer = -1        
        
    return answer