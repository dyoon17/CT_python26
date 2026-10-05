def solution(arr, k):
    answer = []
    count = 0
        
    for i in arr:
        if i not in answer:
            answer.append(i)
            count += 1
        
        if count == k:
            break
            
    if len(answer) < k:
        for _ in range(k - len(answer)):
            answer.append(-1)
            
    return answer