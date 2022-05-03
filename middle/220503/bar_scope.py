print('\n--------------------------------------')

a = 1       # 전역(global)변수
print(a)

def vartest(x) :    # 지역변수 (x 를 a로 사용해도 무관)
    print(x)
    x = x + 10
    return x

# def vartest(a) :    
#     print(a)
#     a = a + 10
#     return a

def vartest() : 
    global a
    print(a)
    a = a + 10
    return a


a=vartest()
print(a)