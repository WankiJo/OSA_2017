init = int(input())
temp = init
count = 0

while(temp != init or count == 0):
    a = temp // 10
    b = temp % 10
    # c = (a + b) // 10
    d = (a + b) % 10
    a, b = b, d
    temp = a * 10 + b
    count += 1


print(count)