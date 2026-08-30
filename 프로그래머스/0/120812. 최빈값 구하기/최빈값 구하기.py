def solution(array):
    answer = 0
    max_cnt = 0
    
    for i in array:
        cnt = array.count(i)
        if cnt > max_cnt:
            max_cnt = cnt
            answer = i 
        elif cnt == max_cnt and i != answer:
            answer = -1
    return answer