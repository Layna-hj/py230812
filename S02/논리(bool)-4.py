"""
#논리
# a와 b가 있다.
# a, b중에 한 명은 참말만 하고 한 명은 거짓말만 한다.
# a, b중 누가 참말만 하는지 누가 거짓말만 하는지 어떻게 알 수 있을까?
# 조건: a, b중 한 사람에게 가서 한 번의 질문을 할 수 있다.
# 그 질문으로 정답을 알아 낼 수 있다.

"""

# 논리형 : bool(boolean)
# 참     : True, 1
# 거짓   : False, 0

#%%

# 같다 : x is y
# 같지 않다 : not x is y

x = 10
y = 20
z = 30

a = (x is y)
b = (not x is y)


print("{0} = {1} is {2}".format(a, x, y))
print("{0} = not {1} is {2}".format(b, x, y))

#%%

# 문자열 비교 
kim = "김씨"
lee = "이씨"

k1 = (kim == lee)
k2 = (kim is lee)
k3 = (not kim is lee)
k4 = (kim != lee)
print(k1, k2, k3, k4)













