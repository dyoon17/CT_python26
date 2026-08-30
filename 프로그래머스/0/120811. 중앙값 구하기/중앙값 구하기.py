def solution(array):
    array.sort()
    
    if len(array) % 2 == 1:
        answer = array[len(array) // 2]
    else:
        print("array의 길이는 홀수입니다.")
    return answer