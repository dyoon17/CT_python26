def solution(lines):
    answer = 0
    

    for x in range(-100, 100):
        cnt = 0
        
        for line in lines:
            if line[0] <= x < line[1]:
                cnt += 1
        if cnt >= 2:
            answer += 1        

    return answer