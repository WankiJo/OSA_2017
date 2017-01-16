t1 = (1, 2, 'a', 'b')

print(t1[0]);
print(t1[2]);

print(t1[1:]);

t2 = (3,4)
print(t1+t2)

print(t2*3);

print(type(t1));

a={1:'a'}
a[2]='b'
print(a);

a['aa']=[1,2]
print(a);

del a['aa']
print(a);

a[t1]='c'
print(a);

print(a.keys())

print(a[(1, 2, 'a', 'b')])
print(a[t1])

s = set("Hello")
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s);
print(s1);
print(s2);

print(s1 & s2);
print(s1 | s2);
print(s1-s2);

s1.add(7)
print(s1);
s1.update([8,9])
print(s1);

s1.remove(9)
print(s1);

a=[1,2,3,4]
while a:
    print(a.pop());

import sys
print(sys.getrefcount(3))

a,b=('python','life')
print(a)
print(a,b)