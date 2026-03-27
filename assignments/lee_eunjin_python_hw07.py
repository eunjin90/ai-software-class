# 함수를 사용해서 회원가입id,pw , 회원정보보기, 회원삭제 , 비밀번호 변경, 종료 만들기

members = {'aaa': '1111', 'bbb': '2222', 'ccc': '3333', 'ddd': '4444'}

# 1. 회원가입
def signup():
    print('*** 회원가입 ***')
    id = input('아이디 입력: ').strip()

    if id in members:
        print('이미 존재하는 아이디입니다.')
        return

    pw = input('비밀번호 입력: ').strip()
    members[id] = pw
    print('회원가입 완료')

# 2. 회원정보 보기
def show_members():
    print('*** 회원정보 ***')
    for k, v in members.items():
        print(k, v)

# 3. 회원 삭제
def delete_member():
    print('*** 회원 삭제 ***')
    id = input('삭제할 아이디 입력: ').strip()

    if id not in members:
        print('존재하지 않는 아이디입니다.')
        return

    pw = input('비밀번호 입력: ').strip()

    if members[id] != pw:
        print('비밀번호가 틀렸습니다.')
        return

    members.pop(id)
    print('회원 삭제 완료')

# 4. 비밀번호 변경
def change_password():
    print('*** 비밀번호 변경 ***')
    id = input('아이디 입력: ').strip()

    if id not in members:
        print('존재하지 않는 아이디입니다.')
        return

    pw = input('현재 비밀번호 입력: ').strip()

    if members[id] != pw:
        print('비밀번호가 틀렸습니다.')
        return

    new_pw = input('새 비밀번호 입력: ').strip()
    members[id] = new_pw
    print('비밀번호 변경 완료')

# 5. 종료
def exit_program():
    print('프로그램을 종료합니다.')
    exit(0)


# 메뉴 반복
while True:
    print('\n===== 메뉴 =====')
    print('1. 회원가입')
    print('2. 회원정보보기')
    print('3. 회원삭제')
    print('4. 비밀번호변경')
    print('5. 종료')

    choice = input('선택: ').strip()

    if choice == '1':
        signup()
    elif choice == '2':
        show_members()
    elif choice == '3':
        delete_member()
    elif choice == '4':
        change_password()
    elif choice == '5':
        exit_program()
    else:
        print('잘못된 입력입니다.')