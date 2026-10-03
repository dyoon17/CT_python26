def solution(todo_list, finished):
    answer = []
    
    for i in range(len(todo_list)):
        for j in range(len(finished)):
            if finished[j] == False:
                if i == j:
                    answer.append(todo_list[i])
    return answer