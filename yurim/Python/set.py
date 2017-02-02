#중복을 허용하지 않는다
#순서가 없다
#s=set()

s=set("hello")
print(s);
s1=set([1,2,3])
l1=list(s1)
print(l1)
t1=tuple(s1)
print(t1)

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print(s1&s2);#교집합
print(s1|s2);#합집합
print(s1-s2);#차집합

s1.update([7,8,9])
print(s1)