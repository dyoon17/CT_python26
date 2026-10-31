def solution(progresses, speeds):
    answer = []
    day = []
    
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            day.append((100 - progresses[i]) // speeds[i])
        else:
            day.append((100 - progresses[i]) // speeds[i] + 1)
    
    m = day[0]
    count = 1
    
    for i in range(1, len(day)):
        if day[i] <= m:
            count += 1
        else:
            answer.append(count)
            m = day[i]
            count = 1
        
    answer.append(count)
                   
    return answer