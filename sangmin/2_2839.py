a = int(input())
min = 0

for i in range(0, 2000):
    for j in range(0, 1000):
        if((3 * i) + (5 * j) == a):
            if(min == 0 or min > i + j):
                min = i + j

if(min == 0):
    min = -1
    print(min)
else:
    print(min)