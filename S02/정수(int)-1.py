#교재 p.70

#자료형 : type(표현식) : int, float, str, object(사용자 자료형, class)
#숫자: 정수형, 실수
#정수형 : 양수, 음수, 실수가 아닌 값
#크기(범위) : 무한대

data1 = 2
data2 = 2.4

#print("data1:", data1)
#print("data2:", data2)


#%%

num = 2
#print("num:",2)

#%%

#자료형
print("data1:", type(data1))  #정수 integer
print("data2:", type(data2))  #float(실수) floating point
print("num:",type(num))  #int
print(type("0.1"))   # 문자열(str)

#%%

#정수형의 크기: 제한이 없다.
num1 = 1234567890
num2 = 12345678901234567890
num3 = 123456789012345678901234567890
#print("num1:",num1, type(num1))
#print("num2:",num2, type(num2))
#print("num3:",num3, type(num3))

#print(num3 + 9)
#print(num3 + 7)

#%%

#s1 = "1234567890"
#s2 = s1 + 7
#print(s2)  #문자와 숫자 더할 수 없음
#TypeError: can only concatenate str (not "int") to str

#문자는 문자끼리 더할 수 있다.
#문자는 문자끼리 더하는 것은 문자열의 결합(뒤에붙임)
s1 = "1234567890"
s2 = s1 + "7"
#print(s2)

#%%
#실수 : 소숫점이 포함된 숫자

#print("num:",num, type(num)) #int

#기존의 변수에 새로운 값을 넣으면 자료형도 바뀌고 값도 변경
num = 1.123
#print("num:",num, type(num))   # float

#%%
#컴퓨터는 이진수(binary)로 숫자를 처리하기 때문에
#실수에 오차가 발생할 수 있다.
#교재 p.71


num1 = 1.000000000000001
num2 = 1.1
print("num1:", num1)
print(num1 + num2)

#결과 : 맨 뒷자리에 4가 추가
#  12345678901234
#2.1000000000000014





























































































