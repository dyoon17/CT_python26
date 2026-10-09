def solution(picture, k):
    answer = []
    
    for pic in picture:
        str = ''
        for i in range(len(pic)):
            str += pic[i] * k
            
        for _ in range(k):
            answer.append(str)
    return answer