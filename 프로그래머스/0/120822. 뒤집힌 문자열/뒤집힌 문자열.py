def solution(my_string):
    # 슬라이싱 개념 사용
    # text[시작:끝:간격] 
    # e.g. text[1:4] -> 1번부터 3번까지
    # 간격 = 2 -> 두칸씩 이동
    # 간격 = -1 -> 한칸씩 거꾸로 이동
    return my_string[::-1]