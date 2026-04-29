import exam25_myTest as mt  # 알리아스(alias) : 별명으로 쓸수 있다 # 여기서는 모듈에만 alias 가능

name = "hello"

print(name)

mt.hello()
mt.prnMsg(name)
print(mt.myTest_msg)


# from 파일 import 함수
#    exam25_myTest2에 다른 여러가지 함수들이 있더라도 전부 제외하고 hello 함수만 쓴다는 뜻 ,콤마로 구분해서 더 쓸수있음
from exam25_myTest2 import hello as h, myTest_msg as msg   # 알리아스(alias) : 여기서는 가져오는 대상(함수, 변수)에만 alias 가능, 대신 모듈에는 alias 못 붙임
h()
print(msg)