#사람이 보기 편하면 좋은 변수
apple = 12
banana = 5

print(apple + banana)
print(apple - banana)
print(apple * banana)
print(apple / banana)

#--------------------------------------------------------------------------------
#문자열 연결(+)을 사용한 방법
#str()을 쓰면 숫자를 문자열로 변환
num1 = 12
num2 = 5

print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))

#--------------------------------------------------------------------------------
#변수를 따로 안 만들고 바로 계산
num3 = 12
num4 = 5

print("덧셈 결과 =", num3 + num4)
print("뺄셈 결과 =", num3 - num4)
print("곱셈 결과 =", num3 * num4)
print("나눗셈 결과 =", num3 / num4)

#--------------------------------------------------------------------------------
#함수이해
#def : 함수를 정의할 때 사용하는 키워드 / 반복되는 계산이나 작업을 한 번만 만들어놓고 여러 번 쓸 수 있게 해주는 도구
#def 함수이름(매개변수):
#    실행할 코드
#    return 반환값  # 없어도 됨

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

num5 = 12
num6 = 5

print(add(num5, num6))
print(sub(num5, num6))
print(mul(num5, num6))
print(div(num5, num6))

#--------------------------------------------------------------------------------
#/, //, % 활용
num7 = int(input("첫 번째 숫자: "))
#input() 함수는 무조건 문자열(str)로 반환 - 숫자 연산을 하려면 문자열을 숫자로 변환해야 함
num8 = int(input("두 번째 숫자: "))
#input() 함수
#int() 형변환

print("덧셈 결과:", num7 + num8)
print("뺄셈 결과:", num7 - num8)
print("곱셈 결과:", num7 * num8)
print("나눗셈 결과:", num7 / num8)      # 실수 나눗셈
print("몫:", num7 // num8)            # 정수 나눗셈
print("나머지:", num7 % num8)         # 나머지