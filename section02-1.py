# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print("Hello")
print("""Hello""")


# Separator 옵션 사용
# 사이값 붙여줌(javascript join 느낌?)
print('T', 'E', 'S', 'T', sep='')
print('2021', '05', '20', sep='-')


# end 옵션 사용
# 줄바꿈을 이어줌
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')


# format 사용
# 순번대로 채워줌(비어있을 경우 순서대로)
print('{} and {}'.format('You', 'Me'))
print('{1} and {0}'.format('You', 'Me'))
print('{a} and {b}'.format(a='You', b='Me'))

# %s: 문자, %d: 정수, %f: 실수
print("%s's favorite number is %d" % ('Wonjae', 3))
print("Test1: %5d, Price: %4.2f" % (77612554, 6534.1235616))
print("Test2: {0:5d}, Price: {1:4.2f}".format(77612554, 6534.1234598))
print("Test2: {a:5d}, Price: {b:4.2f}".format(a=77612554, b=6534.1234598))


"""

\n : 줄바꿈
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""

print('\'Hi\'')
