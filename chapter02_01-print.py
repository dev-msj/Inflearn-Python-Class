# Chapter02-01: 파이썬 완전 기초
# print 사용법(python 버전 3.6 ~ 3.7)
# 참조: https://www.python-course.eu/python3_formatted_output.php

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

print('******* 기본 출력해보기 *******')
print('Hello, World and Python!')
print()

print('******* separator 옵션 사용 - 문자열 사이에 무엇을 넣을지 정의. 기본값은 공백 *******')
print('T', 'E', 'S', 'T', sep='')
print('T', 'E', 'S', 'T', sep='-')
print('python', 'google.com', sep='@')
print()

print('******* end 옵션 사용 - 문자열 마지막에 무엇을 넣을지 정의. 기본값은 줄바꿈 *******')
print('Welcome To', end='')
print(' the black parade', end='@@@')
print(' piano notes')
print()

print('******* file 옵션 사용 - 파일로 출력 *******')
import sys
print('GeeksForGeeks', file=sys.stdout) # 콘솔 출력을 의미
print()

# format 사용(d: 정수, s: 문자열, f: 실수)
# 파이썬 formatting은 크게 2가지 방법이 있다. %를 사용하는 방법과 format 함수를 사용하는 방법이다.
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

print('******* %s - 문자열 출력 *******')
print('%10s' % ('nice',)) # 10자리 확보 후 오른쪽부터 문자열 출력
print('%-10s' % ('nice',)) # 10자리 확보 후 왼쪽부터 문자열 출력(음수 기호는 왼쪽부터 출력을 의미)

print('{:>10}'.format('nice')) # 10자리 확보 후 오른쪽부터 문자열 출력(꺽쇠 방향을 통해 어디부터 채울지 지정)
print('{:<10}'.format('nice')) # 10자리 확보 후 왼쪽부터 문자열 출력(왼쪽 방향 꺽쇠를 사용)
print('{:10}'.format('nice')) # 문자열은 기본적으로 왼쪽부터 출력하므로 꺽쇠를 쓰지 않아도 된다.

print('{:_>10}'.format('nice')) # 10자리 확보 후 오른쪽부터 문자열 출력 후 남는 공간은 언더바로 채우기 => 채우기 문자는 1자리만 가능
print('{:^10}'.format('nice')) # 10자리 확보 후 가운데 정렬

print('%.5s' % ('python study')) # 5자리만 출력 => 점이 없을 경우엔 지정 길이을 넘어도 전부 출력한다.
print('{:10.5}'.format('python study')) # 10자리 확보 후 5자리만 출력
print()

print('******* %d - 정수 출력 *******')
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42)) # 4자리 확보 후 오른쪽부터 정수 출력
print('%4d' % (4212342134)) # 문자열과 동일하게 확보된 길이보다 큰 수는 전부 출력된다.

print('{:<4d}'.format(42)) # 위와 동일한 표현. 문자열과는 다르게 'd'로 타입 표기를 한다.
print('{:4d}'.format(42)) # 문자열과는 다르게 정수 출력은 기본적으로 오른쪽부터 출력한다.
print('{:>4d}'.format(42)) # 당연히 오른쪽 꺽쇠를 쓰면 오른쪽부터 출력한다.
print()

print('******* %f - 실수 출력 *******')
print('%f' % (3.142424243434)) # 기본적으로 소수점 6자리까지 출력
print('%1.4f' % (3.142474243434)) # 소수점 4자리까지 출력. 출력할 소수잠의 길이 지정된 길이보다 길면 반올림하여 출력.
print('%1.18f' % (3.142424243434)) # 정수부 길이 <= 소수부 길이 => 정수 1자리, 소수점 18자리까지 출력. 
print('%06.2f' % (3.142424243434)) # 정수부 길이 > 소수부 길이 => 6자리를 확보하여, 소수점 2자리까지 출력하고 남는 공간은 0으로 채운다. 점도 출력 길이에 포함된다.
print('{:06.2f}'.format(3.142424243434)) # 위와 동일한 표현
