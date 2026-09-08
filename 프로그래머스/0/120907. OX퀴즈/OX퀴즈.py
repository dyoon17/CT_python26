def solution(quiz):
    answer = []
    for S in quiz:
        arr = S.split()
        if arr[1] == "+":
            if int(arr[0]) + int(arr[2]) == int(arr[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(arr[0]) - int(arr[2]) == int(arr[4]):
                answer.append("O")
            else:
                answer.append("X")
                    
    return answer