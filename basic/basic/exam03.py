#input() : 키보드 입력받는 함수
num1 = input('첫번째 정수를 입력하세요')
num2 = input('두번째 정수를 입력하세요')

#int(), float(), str() : type 변환함수

print(num1, type(num1))
num1 = int(num1)
num2 = int(num2)

print('num1 :', num1, 'num2',num2)
print('두 정수의 합 : ',num1+num2)
print('두 정수의 차 : ',num1-num2)
print('두 정수의 곱 : ',num1*num2)
print('두 정수의 나눗셈 : ',num1/num2)
print('두 정수의 몫 : ',num1//num2)
print('두 정수의 나머지 : ',num1%num2)

