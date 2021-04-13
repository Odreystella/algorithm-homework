# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 리턴하는 함수
# 예를 들어 n이 12345이면 [5,4,3,2,1] 리턴

def solution(n):
    answer = [i for i in str(n)]
    return answer[::-1]


# test code

# solution(12345)   
# >> ['5', '4', '3', '2', '1']

# solution(456718)
# >> ['8', '1', '7', '6', '5', '4']

