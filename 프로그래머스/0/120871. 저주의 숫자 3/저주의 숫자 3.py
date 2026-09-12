def solution(n):
    answer = 0
    arr = []
    for num in range(1, 200):        
            if num % 3 == 0:
                continue
            elif "3" in str(num):
                continue      
            else:
                arr.append(num)
        
    answer = arr[n-1]
    return answer