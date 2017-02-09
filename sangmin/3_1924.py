a, b = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
totalDay = 0
for i in range(1, a):
    if(a == 1):
        break
    else:
        totalDay += month[i-1]

totalDay += b

if(totalDay % 7 == 0):
    print("SUN")
elif(totalDay % 7 == 1):
    print("MON")
elif(totalDay % 7 == 2):
    print("TUE")
elif(totalDay % 7 == 3):
    print("WED")
elif(totalDay % 7 == 4):
    print("THU")
elif(totalDay % 7 == 5):
    print("FRI")
else:
    print("SAT")