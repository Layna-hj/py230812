# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:43:07 2023

@author: Layna
"""
#%%

a = 10
b =3

c = a / b
#print("%.0f / %.0f -> %f" % (a,b,c))  # 10 / 3 -> 3.33333
#print("%.d / %d -> %d" % (a,b,c)) # 10 / 3 -> 3

#d : decimal (10진수)

#%%

# 나머지 : %
d = a % b
print("(%d)를 (%d)로 나눈 나머지의 값은 (%d)이다," % (a, b, d))
print("(%d)를 (%d)로 나눈 나머지의 값은 (%f)이다," % (a, b, d))

# 몫은?
m = a // b
print("(%d)를 (%d)로 나눈 몫은 (%d)이다," % (a, b, m))
print("(%d)를 (%d)로 나눈 몫은 (%f)이다," % (a, b, m))








