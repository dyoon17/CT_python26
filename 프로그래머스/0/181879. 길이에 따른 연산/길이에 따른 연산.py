def solution(num_list):
    answer = 0
    answer_sum = 0
    answer_mul = 1
    
    for i in range(len(num_list)):
        if len(num_list) >= 11:
            answer_sum += num_list[i]
            answer = answer_sum
        else:
            answer_mul *= num_list[i]
            answer = answer_mul
            
            
    return answer