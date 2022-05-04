# 예외처리(exception handling) 1 - 예외발생

def multi(a, b) :
    res = a * b
    return res

def divide(a, b) :
    # if b == 0 : return 0
    res = 0

    try :
        res = a / b
    except Exception as e :
        print(f'예외발생 {e}')
    finally :                  # 예외발생 유무와 관계 없이 진행해야 하는 것들
        return res


if __name__ == '__main__' :
    value = 7
    print('곱셉/나눗셈')
    print(divide(6,0))
    print(multi(6,6))
    print('죵료')




