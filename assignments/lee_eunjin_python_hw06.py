# 3월 17일 과제

# 1. 다음의 결과를 보이는 프로그램을 함수를 이용하여 작성하시오.
# 2. 학생 5명의 성적을 입력받아 다음과 같이 출력하는 코드를 작성하시오.

# 1's 성적 : 83
# 2's 성적 : 1000
# 성적은 0~100점 사이로만 입력하세요
# 2's 성적 : 90
# 3's 성적 : 67
# 4's 성적 : 99
# 5's 성적 : 1000
# 성적은 0~100점 사이로만 입력하세요
# 5's 성적 : -34
# 성적은 0~100점 사이로만 입력하세요
# 5's 성적 : 79

# ----------------------------------------------
#     번호            성적            학점
# ----------------------------------------------
#      1              83              B
#      2              90              A
#      3              67              D
#      4              99              A
#      5              79              C
# ----------------------------------------------
# 총점 :
# 평균 :
# 최고점 :
# 최저점 :

def inputScore(num):
    score = int(input(f"{num}'s 성적 : "))
    
    if 0 <= score <= 100:
        return score
    else:
        print("성적은 0~100점 사이로만 입력하세요")
        return inputScore(num)


def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def main():
    scores = []

    for i in range(1, 6):
        scores.append(inputScore(i))

    print("----------------------------------------------")
    print(" 번호   성적   학점")
    print("----------------------------------------------")

    for i in range(5):
        print( " ", i+1, "    ", scores[i], "    ", get_grade(scores[i]))

    print("----------------------------------------------")

    print("총점 :", sum(scores))
    print("평균 :", sum(scores) / 5)
    print("최고점 :", max(scores))
    print("최저점 :", min(scores))

main()


# 2. 3월 16일자 과제를 함수로 작성하시오.

import random

def play(answer, low, high, chance):
    # 기회 다 쓴 경우
    if chance == 0:
        print("기회를 다 소진하셨습니다.")
        print("정답은 [", answer, "]입니다.")
        return

    print(low, "-", high, "사이의 컴퓨터가 생각하는 숫자를 입력하세요 : ", end="")
    user = int(input())

    # 범위 벗어나면 다시
    if user < low or user > high:
        return play(answer, low, high, chance)

    # 정답
    if user == answer:
        print("정답입니다.")
        return

    # 큰 경우
    elif user > answer:
        print(user, "보다 작은수입니다.")
        high = user - 1

    # 작은 경우
    else:
        print(user, "보다 큰수입니다.")
        low = user + 1

    chance -= 1
    print("기회는", chance, "번 남았습니다")

    play(answer, low, high, chance)


def game():
    answer = random.randint(1, 100)
    play(answer, 1, 100, 7)


# 실행
game()




#=============================================================================================================
def guess(low, high, chance):

    # 기회 다 쓴 경우
    if chance == 0:
        print("기회를 다 소진했습니다.")
        print("정답을 알려주세요 😢")
        return

    mid = (low + high) // 2

    print("생각하는 숫자가 [", mid, "]입니까?")
    ans = int(input("정답은 0  작은수면 1  큰수면 2를 입력하세요 : "))

    # 정답
    if ans == 0:
        print("컴퓨터가 정답을 맞췄습니다!")
        return

    # 더 작은 수
    elif ans == 1:
        return guess(low, mid - 1, chance - 1)

    # 더 큰 수
    elif ans == 2:
        return guess(mid + 1, high, chance - 1)

    # 잘못 입력
    else:
        print("잘못 입력했습니다.")
        return guess(low, high, chance)


def game():
    guess(1, 100, 6)


# 실행
game()