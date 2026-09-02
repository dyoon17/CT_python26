def solution(balls, share):
    m_1 = 1
    m_2 = 1
    m_3 = 1
    for i in range(1, balls+1):
        m_1 *= i
    for j in range(1, share+1):
        m_2 *= j
    for k in range(1, balls-share+1):
        m_3 *= k
    answer = m_1 / (m_2 * m_3)
            
    return answer