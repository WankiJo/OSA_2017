# 더하기 기능
result = 0
def adder(num):
    global result
    result += num
    return result

print(adder(3))
print(adder(4))

# 2개의 계산기
result1 = 0
result2 = 0

def adder1(num):
    global result1
    result1 += num
    return result1

def adder2(num):
    global result2
    result2 += num
    return result2

print(adder1(3))
print(adder1(4))
print(adder2(8))
print(adder2(9))

# 클래스 이용
class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(8))
print(cal2.adder(9))

# 클래스 변수
class Service:
    secret = "영구는 배꼽이 두 개다."

pey = Service()
print(pey.secret)

# 클래스 함수
class Service2:
    secret = "영구는 배꼽이 두개다" #유용한 정보
    def sum(self, a, b):                #더하기 서비스
        result = a + b
        print("%s + %s = %s 입니다." % (a, b, result))

pey2 = Service2()
print(pey2.secret)
print(pey2.sum(1,2))

# pey.sum(1, 1)이라는 호출이 발생하면 sum함수의 첫번째 인수인 self에는 호출 시 이용했던 객체(즉, pey라는 아이디)가 자동으로 전달된다. 이러한 이유로 pey.sum(pey, 1, 1)이 아닌 pey.sum(1, 1)으로 사용해야만 하는 것이다.
# pey.sum(1, 1)은 Service.sum(pey, 1, 1)처럼 사용해도 동일한 결과를 얻는다.

# 이름도 넣어주는 서비스
class Service3:
    secret = "영구는 배꼽이 세 개~~"
    def setname(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))

pey3 = Service3()
pey3.setname("Jhao wanqi")
pey3.sum(3, 3)

kim = Service3()
park = Service()
kim.name = "김철수"
park.name = "박뒤박"
print(kim.name, park.name)

# __init__ --> 객체를 만들 때 항상 실행된다.
class Service_init:
    secret = "영구는 init.ver"
    def __init__(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s 입니다." % (self.name, a, b, result))

pey_init = Service_init("jhao_wanki_init")
pey_init.sum(1,3)



######## 사칙연산 클래스 만들기
# a = FourCal()
# a.setdata(4,2)
#print(a.sum())....*, -, /

class FourCal:
    # pass # --> 아무것도 수행하지 않는 문법
    # <class '__main__.FourCal'> -- 출력된 내용.
    def setdata(self, first, second):
        self.first = first
        self.second = second
        print(self.first, self.second)
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setdata(4, 2)

# type 함수는 파이썬이 자체적으로 가지고 있는 내장 함수로 객체의 타입을 출력한다.
print(type(a))

# 다른 호출법
b = FourCal()
FourCal.setdata(b, 4, 2)
print(b.first)

print(b.sum())
print(b.mul())
print(b.sub())
print(b.div())  # --> 2.0으로 출력됨.

class HouseJJo:
    lastname = "조"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." %(self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    # __add__ --> + 연산자를 객체에 사용하면 자동으로 호출됨.
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))

# jo = HouseJJo()
# jo.setname("완기")
# jo.travel("해외")

# __init__ 작성 이후
jo = HouseJJo("완기")
jo.travel("해외2")

# 클래스의 상속과 오버라이딩
class HouseSung(HouseJJo):
    lastname = "성"
    def travel(self, where, day):
        print("%s, %s여행 %s일 가네" % (self.fullname, where, day))

someone = HouseSung("마리")
someone.travel("대만", "fri")

jo.love(someone)
jo + someone

