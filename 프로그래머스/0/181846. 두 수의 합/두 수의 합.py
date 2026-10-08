def solution(a, b):
    answer = ''
    carry = 0
    
    i = len(a) - 1
    j = len(b) - 1
    
    while i >= 0 or j >= 0:
        if i >= 0:
            num1 = int(a[i])
        else:
            num1 = 0
            
        if j >= 0:
            num2 = int(b[j])
        else:
            num2 = 0
        
        total = num1 + num2 + carry
        
        digit = total % 10
        carry = total // 10
        
        answer = str(digit) + answer
        
        i -= 1
        j -= 1
    
    if carry > 0:
        answer = str(carry) + answer
    
    return answer