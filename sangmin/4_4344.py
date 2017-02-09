testcase = int(input())

for i in range(0, testcase):
    count = 0
    total = 0
    a = list(map(int, input().split()))

    for j in range(1, len(a)):
        total += a[j]

    avg = total / a[0]

    for z in range(1, len(a)):
        if(avg < a[z]):
            count += 1

    print("%.3f%%" % round(count / a[0] * 100, 3))
