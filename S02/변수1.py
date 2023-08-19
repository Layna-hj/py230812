# 변수(variable)

#변수는 선언과 동시에 초기값을 지정하여야 한다.
#초기값에 의해서 자료형이 결정
#NameError: name 'a' is not defined
# a

a = 10
print(a, type(a)) # int(integer), 정수

b = "Hello"
print(b, type(b)) # str(string), 문자열

#%%

#[문제] 변수 a, b의 값을 서로 교체하라
a = 10
b = 20

#[풀이]

x = a #대피
a = b
b = x

print("a=", a)
print("b=", b)

#%%

a, b = b, a
print("a=", a)
print("b=", b)
