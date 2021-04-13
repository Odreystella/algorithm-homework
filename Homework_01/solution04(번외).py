# 문자열 길이가 짝수일 때는 가운데 두글자를, 홀수일 때는 가운데 한글자를 반환하는 함수

def solution(s):
    answer = s
    length = len(answer)
    if length % 2 == 1:
        return answer[(length // 2):(length // 2) + 1]
    else:
        return answer[(length // 2) - 1:(length // 2) + 1]


# test code

# solution('abcde')   
# >> 'c'

# solution('asfdjdafk')
# >> 'j'

# solution('abcdjl')
# >> 'cd'