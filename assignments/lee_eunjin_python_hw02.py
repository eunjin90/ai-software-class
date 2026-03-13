# 다음의 결과를 보이는 코드를 작성하시오.
#=================================================================================================================
# 1. 숫자 3개를 입력받아 가장 큰 수를 출력하는 코드를 작성하시오
#     숫자 4개를 입력: 12 6 34 9
#     12, 6, 34, 9 중 가장 큰수 : 34

num = input("숫자 4개를 입력하세요 (예: 12,6,34,9): ")

print("가장 큰 수:", max(map(int, num.split(',')))) #쉼표로 구분할수있게했다 /공백으로 하려면 (' ') 또는 ()

#===========================================================
nums = input("숫자 4개를 입력하세요 (예: 12,6,34,9): ")
a, b, c, d = map(int, nums.split(','))

big = a

if b > big:
    big = b
if c > big:
    big = c
if d > big:
    big = d

print("가장 큰 수:", big)

#===========================================================
a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))
c = int(input("세 번째 숫자: "))
d = int(input("네 번째 숫자: "))

big = a

if b > big:
    big = b
if c > big:
    big = c
if d > big:
    big = d

print("가장 큰 수:", big)

#===========================================================
num = (input('숫자 4개 입력').split())

a =(int(num[0]))
b =(int(num[1])) 
c =(int(num[2])) 
d =(int(num[3])) 

num = a
if b > num:
    num = b
if c > num:
    num = c
if c > num:
    num = c


print(num)

#=================================================================================================================
# 2. 숫자 3개를 입력받아 작은수에서 큰수 순으로 출력하는 코드를 작성하시오
#     숫자 3개를 입력 : 54 2 15
#     2 15 54

nums = input("숫자 3개를 입력: ").split() #공백으로 구분할수있게했다 또는 (' ')
a, b, c = map(int, nums)

# if문으로 큰값 비교
if a <= b and a <= c:  # a보다 b가 크거나같으면 그리고 a보다 c가 크거나같으면 (and 둘다만족)
    if b <= c:          # 둘 다 a보다 큰수라면 b와 c 비교 c가 b보다 크거나같으면 a b c 순 출력
        print(a, b, c)
    else:               # b가 더크면 a c b 순 출력
        print(a, c, b)
elif b <= a and b <= c: # b보다 a가 크거나같으면 그리고 b보다 c가 크거나같으면 (and 둘다만족)
    if a <= c:          # c가 더크면 b a c 순 출력
        print(b, a, c)
    else:               # c가 더크면 b c a 순 출력
        print(b, c, a)
else:  # c가 제일 작은 경우
    if a <= b:
        print(c, a, b)
    else:
        print(c, b, a)

#========================================================두가지경우로 했습니다

a = int(input("a 입력: "))
b = int(input("b 입력: "))
c = int(input("c 입력: "))

# sum이란 변수를 만들어 a를 넣고 비교한다 가장 큰 값 찾기
max_sum = a
if b > max_sum:
    max_sum = b
if c > max_sum:
    max_sum = c
    #최대값구하기

min_sum = a
if b < min_sum:
    min_sum = b
if c < min_sum:
    min_sum = c
    #최소값구하기

mid_sum = (a + b + c) - max_sum - min_sum
    #최대값에서 최소값을빼서 중간값을 구한다 (예: mid_sum = 12 + 6 + 9 - 12 - 6 = 9)

print("작은 수부터:", min_sum, mid_sum, max_sum)

#=================================================================================================================
# 3. 성적을 입력받아 학점을 출력하는 코드를 작성하시오
#     --------------------------------------------
#             범위                    학점
#     --------------------------------------------
#         90 ~ 100                     A
#         80 ~ 89                      B
#         70 ~ 79                      C
#         60 ~ 69                      D
#         0 ~ 59                       F
#     --------------------------------------------

#         성적 입력 : 92
#         92점의 학점은 A입니다

score = int(input("성적 입력: "))

if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score <= 89:
    grade = "B"
elif score >= 70 and score <= 79:
    grade = "C"
elif score >= 60 and score <= 69:
    grade = "D"
elif score >= 0 and score <= 59:
    grade = "F"

# 출력
print(f"{score}점의 학점은 {grade}입니다")

#=================================================================================================================
# 4. 3번 문제에서 성적을 1000점을 입력했다면 " 성적의 범위를 잘못입력하셨습니다" 출력

score = int(input("성적 입력: "))

if 90 <= score <= 100:
    print(f"{score}점의 학점은 A입니다")
elif 80 <= score <= 89:
    print(f"{score}점의 학점은 B입니다")
elif 70 <= score <= 79:
    print(f"{score}점의 학점은 C입니다")
elif 60 <= score <= 69:
    print(f"{score}점의 학점은 D입니다")
elif 0 <= score <= 59:
    print(f"{score}점의 학점은 F입니다")
else:                                           # else : 나머지 경우
    print("성적의 범위를 잘못입력하셨습니다")

#=================================================================================================================
# 5. 물건 값을 입력하고, 지불한 돈의 액수를 입력했을 때 거스름돈을 출력한 후 
#     1000원, 500원, 100원, 50원, 10원의 동전 개수를 출력하는 코드를 작성하시오.

#     물건값을 입력하시오 : 6370
#     지불한 돈의 액수를 입력하시오 : 10000

#     거스름돈 : 3630원
#     1000원 : 3개
#     500원 : 1개
#     100원 : 1개
#     50 : 0개
#     10원 :3개

# 물건 값 입력
price = int(input("물건값을 입력하시오: "))

# 지불한 금액 입력
paid = int(input("지불한 돈의 액수를 입력하시오: "))

# 거스름돈 계산
change = paid - price
print(f"\n거스름돈 : {change}원")

# 동전 계산
coins_1000 = change // 1000       # 1000원 개수
change = change % 1000            # 1000원 제외한 나머지

coins_500 = change // 500
change = change % 500

coins_100 = change // 100
change = change % 100

coins_50 = change // 50
change = change % 50

coins_10 = change // 10
change = change % 10

# 출력
print(f"1000원 : {coins_1000}개")
print(f"500원 : {coins_500}개")
print(f"100원 : {coins_100}개")
print(f"50원 : {coins_50}개")
print(f"10원 : {coins_10}개")

#=================================================================================================================
# 6. 5번 문제에서 지불한 돈의 액수가 물건값보다 작은 경우는 "xxx원이 부족합니다" 메세지 출력
#     물건값을 입력하시오 : 6370
#     지불한 돈의 액수를 입력하시오 : 1000

#     5370원이 부족합니다

# 물건 값 입력
price = int(input("물건값을 입력하시오: "))

# 지불한 금액 입력
paid = int(input("지불한 돈의 액수를 입력하시오: "))

# 지불 금액 확인
if paid < price:
    shortage = price - paid
    print(f"\n{shortage}원이 부족합니다")
else:
    # 거스름돈 계산
    change = paid - price
    print(f"\n거스름돈 : {change}원")

    # 동전 계산
    coins_1000 = change // 1000
    change = change % 1000

    coins_500 = change // 500
    change = change % 500

    coins_100 = change // 100
    change = change % 100

    coins_50 = change // 50
    change = change % 50

    coins_10 = change // 10
    change = change % 10

    # 출력
    print(f"1000원 : {coins_1000}개")
    print(f"500원 : {coins_500}개")
    print(f"100원 : {coins_100}개")
    print(f"50원 : {coins_50}개")
    print(f"10원 : {coins_10}개")

#=================================================================================================================
# 7. 5번문제에서 만일 동전이 필요없다면 출력에서 제외

#     물건값을 입력하시오 : 6370
#     지불한 돈의 액수를 입력하시오 : 10000

#     거스름돈 : 3630원
#     1000원 : 3개
#     500원 : 1개
#     100원 : 1개
#     10원 :3개

# 물건 값 입력
price = int(input("물건값을 입력하시오: "))

# 지불한 금액 입력
paid = int(input("지불한 돈의 액수를 입력하시오: "))

# 거스름돈 계산 (음수 가능)
change = paid - price
print(f"\n거스름돈 : {change}원")

# 동전 계산
coins_1000 = change // 1000
change = change % 1000

coins_500 = change // 500
change = change % 500

coins_100 = change // 100
change = change % 100

coins_50 = change // 50
change = change % 50

coins_10 = change // 10
change = change % 10

# 출력 (0인 동전은 출력하지 않음)
if coins_1000 != 0:
    print(f"1000원 : {coins_1000}개")
if coins_500 != 0:
    print(f"500원 : {coins_500}개")
if coins_100 != 0:
    print(f"100원 : {coins_100}개")
if coins_50 != 0:
    print(f"50원 : {coins_50}개")
if coins_10 != 0:
    print(f"10원 : {coins_10}개")


#===================# 6번과 같이 해도되지만 문제에 5번문제에서 라고 하셨기에 아예 계산이 안되도록 했습니다
                    # 지불한 금액이 부족하면 마이너스가 되기때문에 거스름돈이 있을 때만 계산하게 해줬습니다
# 물건 값 입력
price = int(input("물건값을 입력하시오: "))

# 지불한 금액 입력
paid = int(input("지불한 돈의 액수를 입력하시오: "))

# 거스름돈 계산
change = paid - price

if change >= 0:  # !!!!!
    print(f"\n거스름돈 : {change}원")

    # 동전 계산
    coins_1000 = change // 1000
    change = change % 1000

    coins_500 = change // 500
    change = change % 500

    coins_100 = change // 100
    change = change % 100

    coins_50 = change // 50
    change = change % 50

    coins_10 = change // 10
    change = change % 10

    # 출력 (0개인 동전은 출력하지 않음)
    if coins_1000 > 0:
        print(f"1000원 : {coins_1000}개")
    if coins_500 > 0:
        print(f"500원 : {coins_500}개")
    if coins_100 > 0:
        print(f"100원 : {coins_100}개")
    if coins_50 > 0:
        print(f"50원 : {coins_50}개")
    if coins_10 > 0:
        print(f"10원 : {coins_10}개")