def solution(answers):
    answer = []
    student = [0, 0, 0]
    m = 0
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    
    for i in range(len(answers)):
        if answers[i] == a1[i % 5]:
            student[0] += 1
        if answers[i] == a2[i % 8]:
            student[1] += 1
        if answers[i] == a3[i % 10]:
            student[2] += 1
            
    m = max(student)    
    for i in range(len(student)):
        if student[i] == m:
            answer.append(i+1)
        
            
    return answer