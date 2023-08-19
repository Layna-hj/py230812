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

# 크기 비교 : 왼쪽 기준
# 크다 : >
# 작다 : <

x = 1
y = 2

a = (x > y)
b = (x < 2)

#print("%d > %d -> %") % (x, y, a))
#print("{0}> {1} -> {2}".format(x, y, a))

print("{0} = {1} > {2}".format(a, x, y))

print("%d = %d > %d" % (a, x, y))
print("%d = %d > %d" % (a, x, y))

#%%

print("%s = %d > %d" % (a, x, y))
print("%s = %d > %d" % (b, x, y))

#%%

c = (True > False)
d = (True < False)


#%%

x = True
y = False
c = (x > y)
d = (x < y)
print("%s = %d > %d" % (c, x, y))
print("%s = %d > %d" % (d, x, y))





















