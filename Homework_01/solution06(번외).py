# 두 정수 a, b가 주어졌을 때 그 사이에 속한 모든 정수의 합을 리턴하는 함수
# 예를 들어 a =3, b = 5인 경우, 12(= 3 + 4 + 5)를 리턴

# 제한 조건
# - a, b가 같은 경우 둘 중 하무 수나 리턴함
# - a와 b의 대소관계는 정해져있지 않음
# - a와 bsms -10,000,000이상 10,000,000 이사인 정수

def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))


# range([start, stop, step)
# ex) list(range(5))  >> [0, 1, 2, 3, 4]    
# ex) list(range(5, 10))  >> [5, 6, 7, 8, 9]    
# ex) list(range(1, 10, 2))  >> [1, 3, 5, 7, 9]    


# test code

# solution(3,5)
# >> 12

# solution(5,3)
# >> 12

# solution(3,3)
# >> 3

