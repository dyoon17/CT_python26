def solution(num, total):
    answer = []
    answer.append(total // num)
    
    if num % 2 == 1:
        for i in range(total // num - 1, total // num - num // 2 - 1, -1):
            answer.insert(0, i)
        for i in range(total // num + 1, total // num + num // 2 + 1):
            answer.append(i)
    else:
        for i in range(total // num - 1, total // num - num // 2, -1):
            answer.insert(0, i)
        for i in range(total // num + 1, total // num + num // 2 + 1):
            answer.append(i)
        
    return answer