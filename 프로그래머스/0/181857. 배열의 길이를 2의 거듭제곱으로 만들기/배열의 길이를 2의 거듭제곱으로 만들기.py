def solution(arr):
    answer = arr
    num = 1
    
    while num < len(arr):
        num *= 2
        if num > len(arr):
            break
    
    for i in range(num - len(arr)):
        answer.append(0)
    return answer