######## 함수 구조

def sum(a, b):
    return a +b

a = 3
b = 4
c = sum(a,b)
print(c)

def sum2(a, b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))

sum2(3,5)

# 함수의 결과값은 언제나 하나이다.
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum +i
    print(sum)
# -->
sum_many(1,2,3,4,5,6,7)

# return 사용
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." %nick)

say_nick('야호')
say_nick('바보')


# 입력 인수에 초깃값 미리 설정하기
# 입력 인수 순서를 맞춰 주어야 한다.
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자")
    else:
        print("여자")

say_myself('wk', 25)

#vartest_global.py
a =1
def vartest():
    global a
    a = a +1

vartest()
print(a)


######## 사용자 입력과 출력
a = input()
print(a)

# 인수 end를 이용해 끝 문자 지정
for i in range(10):
    print(i, end='    ')

# w 쓰기모드 r 읽기모드, a 추가모드
f = open("alpha.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)
    print(f)
f.close()

#readlines() 함수 이용하기
f2 = open("alpha.txt", 'r')
lines = f2.readlines()
for line in lines:
    print(line)
f.close()

# with문을 이용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동close
with open("foo.txt", "w") as f:
    f.write("Life is..")
    print(f)

