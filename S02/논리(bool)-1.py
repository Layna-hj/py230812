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

t = True
f = False

#print('t=', t, type(t))
#print('f=', f, type(f))

#%%

# t와 f는 같은가?
tf = t == f
print('tf=',tf) # False

# t와 f는 같지 않은가?
tf = t != f
print('tf=',tf)  # True

#%%

a = (1 == 1)  # True
b = (1 != 1)  # False
c = (a == b)  # False  <- True == False
d = (a != b)  # True   <- True != False
 
print('a=', a) # True
print('b=', b) # False
print('c=', c) # False
print('d=', d) # True





































