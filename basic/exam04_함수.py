# 1-100점 사이의 성적을 입력받아 학점을 출력하는 코드를 작성

# 키보드로 0~100점 사이의 성적을 입력받아 호출자에게 전달
def inputScore():
    score = int(input('0~100점 사이의 성적을 입력하세요 : '))
    return score

# 호출자가 넘겨준 성적을 이용하여 학점 구한 후 호출자에게 전달
def getGrade(score):
    grade = 'F'
    if score >= 90: grade = 'A'
    elif score >= 80: grade = 'B'
    elif score >= 70: grade = 'C'
    elif score >= 60: grade = 'D'

    return grade

# 호출자가 전달해준 성적, 학점을 출력하는 기능
def printResult(score, grade):
    print(f'{score} 성적의 학점은 {grade}이다')
    return score,grade

def printStudent(list):
    print(f'{list[0]} 성적의 학점은 {list[1]}')
    return list

score = inputScore()
grade = getGrade(score)
stuData = [score, grade]
# printResult(score, grade)
printStudent(stuData)