def solution(n, control):
    answer = n
    for key in control:
        if key == 'w':
            answer += 1
        elif key == 's':
            answer -= 1            
        elif key == 'd':
            answer += 10       
        elif key == 'a':
            answer -= 10
    return answer