# 정수 num 홀짝 판별하는 함수

# 제한조건: 
# - num은 int 범위의 정수
# - 0은 짝수

def solution(num):
    answer = num
    return "Even" if answer % 2 == 0 else "Odd"
    
