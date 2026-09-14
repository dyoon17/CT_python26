def solution(bin1, bin2):
    i = len(bin1) - 1
    j = len(bin2) - 1
    carry = 0
    answer = []
    
    while i >= 0 or j >= 0:
        if i >= 0:
            num1 = int(bin1[i])
        else:
            num1 = 0
        if j >= 0:
            num2 = int(bin2[j])
        else:
            num2 = 0
        
        total = num1 + num2 + carry
        answer.insert(0, str(total % 2))
        carry = total // 2
        i -= 1
        j -= 1
        
    if carry == 1:
        answer.insert(0, "1")
    
    answer = ''.join(answer)
    
    return answer