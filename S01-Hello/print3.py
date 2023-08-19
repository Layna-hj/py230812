# print() 함수
# print(파라미터, ...)

x = 10
y = 20
z = 30

#print() 함수의 sep 기본값을  (공백)
print(x, y, z) 
#print(x,y,z, sep=' ') #10 20 30

#%%

#prnt(x,y,z, sep=' ') #102030
#print(x,y,z, sep=' ') #10,20,30
#print(x,y,z, sep=' ') # 10, 20, 30

#%%

#[문제]
# 전화번호: 국번, 가운데번호, 끝번호를 변수에 담아 출력하라.

# 각 번호의 사이를 '-'로 구분

# 각 번호의 사이를 '.'로 구분

"""
tel1 =" 010"
tel2 =" 1234"
tel3 =" 4567"
print(tel1, tel2, tel3, sep='-')
print(tel1, tel2, tel3, sep='.')
"""

#%%

print("전화번로 입력")
tel1 = input("국번을 입력하세요")
tel2 = input("가운데 번호를 입력하세요:")
tel3 = input("마지막 번호를입력하세요:")
print(tel1, tel2, tel3, sep='-')



















