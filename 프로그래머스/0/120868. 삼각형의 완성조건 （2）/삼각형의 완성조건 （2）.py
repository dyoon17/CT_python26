def solution(sides):
    answer = 0
    sum = sides[0] + sides[1]
    
    for i in range(1, sum):
        if i >= max(sides):
            answer += 1
        else:
            if i + min(sides) > max(sides):
                answer += 1
            else:
                continue
            
    return answer