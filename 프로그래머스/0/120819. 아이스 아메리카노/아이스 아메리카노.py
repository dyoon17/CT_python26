def solution(money):
    cnt = money // 5500
    left = money % 5500
    answer = [cnt, left]
            
    return answer