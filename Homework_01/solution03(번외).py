# n이 양의 정수 x의 제곱근일 경우, (x+1) 제곱을 반환하고, 아닐경우 -1을 반환하는 함수

def solution(n):
    x = n ** 0.5
    if (x * x == n):
        return (x + 1) ** 2
    else:
        return -1


# test code

# solution(121)   
# >> 144.0

# solution(3)
# >> -1

