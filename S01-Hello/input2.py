# input 명령어
# 키보드로부터 내용을 입력 받는 명령어
# 변수 =input("안내문자")
#
# Type(변수) : 변수가 가지고 있는 자료형을 알려 준다.


abc = input("값을 입력하세요")
print(abc)
print(type(abc)) # <class 'str'>, string(문자열)

#%%
#print("값을 입력하세요", end='')

#안내 문구 없이 입력을 
abc = input()
print(abc)