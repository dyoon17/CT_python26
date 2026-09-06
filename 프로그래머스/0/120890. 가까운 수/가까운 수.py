def solution(array, n):
    answer = 0
    min_diff = 101
    
    for i in array:
        diff = abs(i-n)
        if diff < min_diff: # i의 값을 반영한 새로운 diff가 더 작을 경우
            min_diff = diff # 계산한 diff를 새로운 min_diff로 업데이트
            answer = i  # 가까운 수를 answer에 저장
        elif diff == min_diff and i < answer:
            answer = i
    
    return answer