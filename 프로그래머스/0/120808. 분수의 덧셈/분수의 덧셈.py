def solution(numer1, denom1, numer2, denom2):
    new_n = numer1 * denom2 + denom1 * numer2
    new_d = denom1 * denom2
    
    i = 2
    while i <= min(new_n, new_d):
        if new_n % i == 0 and new_d % i == 0:
            new_n //= i
            new_d //= i
        else:
            i += 1
    return [new_n, new_d]