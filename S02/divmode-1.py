# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:43:07 2023

@author: Layna
"""
#%%
# 나머지 : %, divmod(x,y)

a = 10
b = 3
d = a % b
#print("(%d)를 (%d)로 나눈 나머지의 값은 (%d)이다," % (a, b, d))
#print("(%d)를 (%d)로 나눈 나머지의 값은 (%f)이다," % (a, b, d))

# 몫은?
m = a // b  #정수 나누기
#print("(%d)를 (%d)로 나눈 몫은 (%d)이다," % (a, b, m)) 
#print("(%d)를 (%d)로 나눈 몫은 (%f)이다," % (a, b, m))

#%%

# divmod(x, y) 함수 : 몫과 나머지를 동시에 구함

# 2개 명령어 동시 실행 효과
# 1. a // b
# 2. a % b

g = divmod(a, b)
print("{} = divmod({},{})".format(g,a,b))

x, y = divmod(a, b)
print("{} = divmod({},{})".format(x,y,a,b))

print("몫:x=", x)
print("나머지:y=", y)

print("몫:g[0] =",g[0])
print("나머지:g[1] =", g[1])

#%%

m = a // b
d = a % b
x, y = m, d
print("x=", x)
print("y=", y)
















