def solution(num_list):
    N = len(num_list)
    e_cnt = 0
    o_cnt = 0
    
    for i in range(N):
        if num_list[i] % 2 == 0:
            e_cnt += 1
        else:
            o_cnt += 1
    answer = [e_cnt, o_cnt]
    return answer