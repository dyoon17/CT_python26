def solution(numlist, n):
    answer = []
    num_diff = 9999
    numlist.sort()
    
    for num in numlist:
        if abs(num - n) < num_diff:
            num_diff = abs(num - n)
            answer.insert(0, num)
        elif abs(num - n) > num_diff:
            inserted = False
            
            for i in range(1, len(answer)):
                if abs(num - n) < abs(n - answer[i]):
                    answer.insert(i, num)
                    inserted = True
                    break
                    
                elif abs(num - n) == abs(n - answer[i]):
                    if num > answer[i]:
                        answer.insert(i, num)
                        inserted = True
                        break
    
            if inserted == False:
                answer.append(num)                 
                  
    return answer