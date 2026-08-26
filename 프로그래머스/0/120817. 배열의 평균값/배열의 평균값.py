def solution(numbers):
    n = len(numbers)
    total = 0
    
    for i in range(n):
        total += numbers[i]
    answer = total / n
    return answer