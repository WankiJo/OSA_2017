a = list(input())

check = 0
for i in range(0, len(a)):
    if(check == 10):
        print('')
        check = 0

    print(a[i], end='')
    check += 1