###
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i = i + 1
    return result

print(GuGu(3))


###
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)


###
def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(20, 10))