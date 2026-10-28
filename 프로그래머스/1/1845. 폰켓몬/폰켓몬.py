def solution(nums):
    answer = 0
    A = []
    
    for i in nums:
        if i not in A:
            A.append(i)
            
    if (len(nums) // 2) > len(A):
        answer = len(A)
    else:
        answer = len(nums) // 2
    
    return answer