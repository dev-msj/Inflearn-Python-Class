# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n) # 700
print(type(n)) # <class 'int'>

# 동시 선언
x = y = z = 700

# 출력
print(x, y ,z) # 700 700 700

#선언
var = 75

# 출력
print(var) # 75
print(type(var)) # <class 'int'>

# 재 선언
var = "Change Value"

# 출력
print(var) # Change Value
print(type(var)) # <class 'str'>


# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔에 출력

# 예1)
print(300) # 오브젝트 생성 후 값 300을 생성 후 출력

# 예2)
# n -> 777
n = 777 # 오브젝트 생성 후 값 300을 생성하여 n이 참조

print(n)
print(type(n))

m = n # n이 가리키는 오브젝트의 주소를 m도 참조
# m-> 777 <- n

print(m, n)
print(type(m), type(n))

m = 400 # 400 값을 가지는 오브젝트를 새로 생성하고 m이 참조
# m-> 400, 777 <-n

print(m)
print(type(m))


# id(identity)확인 : 객체의 고유값 확인
m = 800
n  = 655

print(id(m)) # 800값을 가지는 오브젝트의 주소값
print(id(n)) # 655값을 가지는 오브젝트의 주소값


m = 800
n  = 800

# 같은 오브젝트 참조
# => 파이썬은 오브젝트 풀을 사용하여 동일한 값의 변수가 재사용될 수 있도록 한다.
print(id(m))
print(id(n))

# 다양한 변수명 선언 방법
# Camel Case :  numberOfCollegeGraduates
# Pascal Case :  NumberOfCollegeGraduates
# Snake Case :  number_of_college_graduates => 파이썬에서 주로 사용

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능하다.
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""