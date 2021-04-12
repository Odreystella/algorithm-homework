# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수 

# 제한조건:
# - s는 길이 1이상, 길이 8 이하인 문자열

def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit() == True:
        return True
    else:
        return False