"""
#교재 p.74

int, float 변환
eval() 함수 : 파라미터 문자열로 전달된 코드를 실행
    
    
"""
#%%
10 + 20
eval("10 + 20")
y = 10 + 20

# eval로 전달된 파이썬 코드인 "y"를 실행 시켜서 변수 x에 전달
# eval에 전달된 파라미터의 자료형은 출력을 위한 문자열이 아니다.
x = eval("y") #문자의 y가 아니라 변수 값을 실행시킨 것.
print(x, y) # 30 30


#%%

# input() 함수가 리턴하는 값의 자료형은 문자열(str)
height = input("키 정보 입력:")
print("height:" , height, type(height)) # height: 178.9 <class 'str'>

#%%

#입력에서 "홍길동"을 넣으면 에러
# NameError: name '홍길동' is not defined
#숫자를 넣으면 해당하는 자료형으로 변환이 돼서 height에 저장이 된다.
홍길동 = "당신은 누구?"


height = eval(input("키 정보 입력:"))
print("height:" , height, type(height))

#%%

10
홍길동


#%%



























