
#def  함수생성예약어

#초기값 설정
def sum(a,b=0):
    return a+b

print(sum(3))

#여러 개의 입력값
def sum_many(*args):
    sum=0
    for i in args:
        sum = sum+i
        return sum

result=sum_many(1,2,3,4,5,6,7,8,9)
print(result)