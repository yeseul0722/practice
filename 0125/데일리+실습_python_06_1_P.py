# 1. 주민등록번호 앞의 6자리는 생년월일이고, 뒤 7자리는 성별, 지역, 오류검출코드이다.     
# 주민등록번호를 입력받아 주민등록번호 뒷자리를 비식별화하는 함수 de_identify 를 만들어라.
# 해당 변수는 인자를 하나만 받는다.
# 함수 정의시 매개변수는 한 개면 된다.
def de_identify(string):
    # 문자열을 받아온 다음, 그 문자열이 가진 내용중
    # '-'에 해당하는 부분을 없앨 것이다.
    # 반복문을 통해서 넘겨받은 문자열을 하나하나 비교한 뒤, 특정 문자열을 제외한
    # 문자열을 만들어서 반환해야 한다.
    # result = ''
    # for char in stirng:
    #     if char == '-':
    #         continue
    #     else:
    #         result += char

    #문자열이 가진 특성상 원본을 바꿀수는 없으니 변경된 값을 반환
    result = string.replace('-','')

    print(result[:6] + '*' * 7) #'970103 + *******'

    result = list(result)
    result[6:] = ['*'] * 7
    return ''.join(result)
    # print(result)

    # real_result = ''
    # for char in result:
    #     idx += 1
    #     if idx >= 6:
    #         real_result += '*'
    #     else:
    #         real_result += char
    #     idx += 1
    # print(result)

# A. 입력예시
print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 
