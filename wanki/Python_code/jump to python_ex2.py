a = 1
b = 2
c = b - a
print(c)

d=7%3
print(d)

e = 7/4
f = 7//4
print(e)
print("f=")
print(f)

food = "Python's favorite food is perl"
print(food)

food2 = """Python's
favorite food is perl"""
print(food2)

a = "python"
print("a*2 =")
print(a*2)

# indexing
a= "Life is too short, You need Python"
print(a[5])
print(a[3])
print(a[-1])
print(a[0])
print(a[-0])

b=a[0]+a[1]+a[2]+a[3]+a[4]
print(b)

print(a[0:4])

print("I eat {0} apples".format(3))
print("I eat {0} apples".format("null"))

print("I eat {0} apples {1}".format(3,"null"))
print("I eat {0} apples {da}".format(3, da="null"))

print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
print("{0:!>10}".format("hi"))

y=3.432422222222222222273738
print("{0:0.4g}".format(y))

print("{{and}}".format())

a= [1,2,3,['a','b','c',['af']]]
print(a[0])
print(a[3])

print(a[-1][3][0])
print(a[-1][3])

print(a*2)

a= [1,2,3]
b= [5,6,7]
print(a+b)

print(b*3)

print(a[2])
print(str(a[2])+"hi")
st = str(a[2]) + "hi"
print(st)

print(a[1:3])

a[1:2] = ['a','b']
print(a)

a[2] =  ['a','b','c','d']
print(a)
a[1:2]= []
print(a)
del a[0]
print(a)

a.append(1)
print(a)

a.append([8,9])
print(a)

d=[1,3,65,2]
d.sort()
print(d)

d.reverse()
print(d)

print(d.index(1))

d.insert(0,99)
print(d)

#첫번쨰 3 제거
d.remove(3)
print(d)

#3번째 요소 돌려주고 제거
print(d.pop(0))
print(d)

print(d.count(2))

d.extend([88,77])
print(d)
