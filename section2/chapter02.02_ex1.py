# Chapter02-02-ex1: 파이썬 완전 기초
# print 사용법(python 버전 3.10 이상)

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

### 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Lee'


# 출력1 - % 사용
ex1 = 'n = %s, s = %s, sum=%d' % (n, text, (x + y)) # %d
print(ex1)


# 출력2 - format 사용
ex2 = 'n = {n}, s = {serialno}, sum={sum}'.format(n=n, serialno=text, sum=x + y)
print(ex2)


# 출력3 - f-string 사용
ex3 = f'n = {n}, s = {text}, sum={x + y}'
print(ex3)

print()
print()


# 출력4(다양한 f-string 연습)
k = 98

print(f"k 2진수: {k:b}, k 8진수: {k:o}")
print(f"k 16진수 - l:{k:x}, U:{k:X}")

print()
print()


# 구분기호
m = 10000000000

print(f"m: {m:,}") # 천단위로 구분하기

print()
print()


# 정렬
# ^ : 가운데 , < : 왼쪽 , > : 오른쪽
t = 20

print(f"t :{t:10}") # 10자리 확보 후 오른쪽부터 정수 출력
print(f"t center: {t:^10}") # 10자리 확보 후 가운데 정렬
print(f"t left: {t:<10}") # 10자리 확보 후 왼쪽부터 정수 출력
print(f"t right: {t:>10}") # 10자리 확보 후 오른쪽부터 정수 출력

print()
print()


# 채우기
print(f"t:{t:-^10}") # 10자리 확보하고 가운데 정렬 후 남는 공간은 -로 채우기
print(f"t:{t:#^10}") # 10자리 확보하고 가운데 정렬 후 남는 공간은 #로 채우기