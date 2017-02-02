######## Tuple

# 리스트와 tuple의 다른 점은 값을 변화시킬 수 없다. 상황에 따른 사용.
t1=()
# 단지 1개의 요소만 가질 때는 요소 뒤에 콤마(,) 붙여야 함.
t2=(1,)
t3=(1,2,3)
t4=1,2,3
t5=('a','b',('ab','cd'))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

t1 = (1,2,'a','b')
# del t1[0] --> 오류
print(t1)

# t1[0] = 'c' --> 오류
print(t1)

print(t1[0])
print(t1[3])

print(t1[2:])

print(t1+t2)
print(t1*4)

######## Dic

dic = {'name':'pey', 'phone':'01045145683'}

# Key 정수값, Value 문자
z = { 1: 'hi'}
print(z)

# Value에 List도 가능
y = {'a': [1,2,3]}
print(y)

#쌍 추가
z[2] = 'two'
print(z)

z['3name'] = 'wk'
print(z)

z['4']='wkwkwk'
print(z)

# 지울 key값 삽입
del z['4']
print(z)

grade = {'pey':10, 'julliet': 99}
print(grade['pey'])

num = {1:'a', 2:'b'}
print(num)

print(z.keys())
print(z.values())
print(z.items())
print("next")
for v in z.keys(), z.values(), z.items():
    print(v)

lis = list(z.keys())
print(lis)

print(z.get(1))
# nokey == 거짓
print(z.get('nokey'))

# key 있는지 여부 확인
print(1 in z)
print('hi' in z)

print(z.clear())

######## Set

# 괄호에 리스트나 문자열 입력하여 만들 수도 있다.
s1 = set([1,2,3])
s2 = set("Hello")
print(s1, s2)

# Set은 중복허용 X, 순서 없음(Undrdered)

# 교집합 s1 & s2, s1.intersection(s2)
# 합집합 s1 | s2 ,s1.union(s2)
# 차집합 s1 - s2, s1.difference(s2)

# 더하기 s1.add(3)

# 여러값 추가
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

# 특정 값 제거 remove
s1.remove(2)
print(s1)

# .pop()
a = [1,2,3,4]
while a:
    print(a.pop())

# 변수 삭제 del()
a= 1
del(a)

# 리스트 복사
a = [1,2,3]
b = a
a[1] = 4
print(a,"<->",b)

# from copy import copy
# d = copy(c)   =====    d = c[:]
c = [1,2,3]
d = c[:]
c[1] = 4
print(c,"<->",d)

print(a is b)
print(d is c)
