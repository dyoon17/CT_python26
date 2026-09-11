def solution(my_string):
    answer = 0
    new = my_string
    for i in my_string:
        if i.isdigit() == False:
            new = new.replace(i, ' ')
        else:
            continue
        
    new = new.split()
    for i in range(len(new)):
        answer += int(new[i])
    return answer