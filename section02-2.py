# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 변수 선언
myName = 'Goodboy'

# 변수 선언(한글)-권장X
이름 = "좋은 사람"


# 조건문
if myName == "Goodboy":
    print("ok")


# 반복문(구구단)
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i * j)

# 함수 선언


def greeting():
    print('안녕하세요, 반갑습니다')


greeting()


# 클래스
class Cookie:
    pass


# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
